from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Collection, Product, Review
from .serializers import CollectionSerializer, ProductSerializer, ReviewSerializer
from .permissions import IsGuestOrReadOnly, IsMemberOrAdmin, IsAdmin, IsReviewAuthorOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

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
        elif self.action in ['create']:
            self.permission_classes = [IsMemberOrAdmin]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Use custom permission to ensure only the review author can modify or delete their review
            self.permission_classes = [IsAuthenticated, IsReviewAuthorOrReadOnly]
        return super().get_permissions()

    def get_queryset(self):
        product_id = self.kwargs.get('product_pk')
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author of the review
        serializer.save(user=self.request.user)


class RegisterUser(APIView):
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Allow any user to access

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        # group_name = request.data.get("group")  # Accept group name from request

        if not username or not password or not email:
            return Response({"error": "All fields are required."}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=400)

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Add the user to the specified group
            group = Group.objects.get(name="guest")
            user.groups.add(group)

            return Response({"message": f"User registered and added to guest group!"}, status=201)
        except Group.DoesNotExist:
            return Response({"error": "Specified group does not exist."}, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token or logout failed."}, status=status.HTTP_400_BAD_REQUEST)


class GetUserRole(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.groups.filter(name='admin').exists():
            role = 'admin'
        elif user.groups.filter(name='member').exists():
            role = 'member'
        elif user.groups.filter(name='guest').exists():
            role = 'guest'
        else:
            role = 'unknown'
        return Response({'role': role}, status=status.HTTP_200_OK)