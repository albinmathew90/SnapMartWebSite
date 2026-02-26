from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()  # in rupees

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    ]

    razorpay_order_id = models.CharField(max_length=255, unique=True)
    razorpay_signature = models.CharField(max_length=500, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True, unique=True)

    amount = models.IntegerField()
    products = models.TextField(blank=True, null=True)  # store product names as text

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="processing"
    )

    is_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.razorpay_order_id} - {self.status}"


