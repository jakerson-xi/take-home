from django.db import models
from decimal import Decimal
# Create your models here.


class Purchase(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    sold_to = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    or_number = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=50, decimal_places=2, default=Decimal("0.00"))
    quantity = models.PositiveSmallIntegerField(default=1)
    remarks = models.TextField(default="", null=True, blank=True)

