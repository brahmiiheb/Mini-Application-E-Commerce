# products/models.py
from xml.dom import ValidationErr
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional description
    price = models.FloatField()
    stock = models.IntegerField()

    def clean(self):
        # Custom validation to ensure price is positive and stock is >= 0
        if self.price <= 0:
            raise ValidationErr("Le prix doit être positif.")
        if self.stock < 0:
            raise ValidationErr("Le stock ne peut pas être inférieur à 0.")

    def __str__(self):
        return self.name
