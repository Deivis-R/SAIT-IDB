from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("view_collection", "Can view collection"),
            ("add_collection", "Can add collection"),
            ("change_collection", "Can change collection"),
            ("delete_collection", "Can delete collection"),
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    collection = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("view_product", "Can view product"),
            ("add_product", "Can add product"),
            ("change_product", "Can change product"),
            ("delete_product", "Can delete product"),
        ]

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating from 1 to 5
    comment = models.TextField()

    class Meta:
        permissions = [
            ("view_review", "Can view review"),
            ("add_review", "Can add review"),
            ("change_review", "Can change review"),
            ("delete_review", "Can delete review"),
        ]

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'