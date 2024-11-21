from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Collection, Product, Review
from .serializers import CollectionSerializer, ProductSerializer, ReviewSerializer
from .permissions import IsGuestOrReadOnly, IsMemberOrAdmin, IsAdmin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only admins can create, update, or delete collections
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            # Guests have read-only access
            permission_classes = [IsGuestOrReadOnly]
        return [permission() for permission in permission_classes]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only admins can create, update, or delete products
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            # Guests have read-only access
            permission_classes = [IsGuestOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        collection_id = self.kwargs.get('collection_pk')
        if collection_id:
            return Product.objects.filter(collection_id=collection_id)
        return super().get_queryset()


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsGuestOrReadOnly]
        elif self.action in ['create', 'update', 'partial_update']:
            self.permission_classes = [IsMemberOrAdmin]
        elif self.action == 'destroy':
            self.permission_classes = [IsAdmin]
        return super().get_permissions()

    def get_queryset(self):
        product_id = self.kwargs.get('product_pk')
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return super().get_queryset()


class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            raise ValidationError("Username, password, and email are required.")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
