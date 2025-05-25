from django.db import models
from django.contrib.auth import get_user_model

from backend.apps.products.models import Product

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Jamlanyapti"),
        ("processing", "Yetkizilmoqda"),
        ("shipped", "Olib ketishingiz mumkin"),
        ("delivered", "Olib ketgan"),
        ("cancelled", "Bekor qilingan"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # snapshot of product price

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="shipping_address")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user} - {self.address}"
