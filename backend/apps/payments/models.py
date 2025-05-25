from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Payment(models.Model):
    PAYMENT_METHODS = [
        ("click", "Click"),
        ("payme", "Payme"),
        ("cash", "Naqd"),
    ]

    STATUS_CHOICES = [
        ("pending", "Kutilmoqda"),
        ("paid", "To'landi"),
        ("failed", "Muvaffaqiyatsiz"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount} {self.method} [{self.status}]"
