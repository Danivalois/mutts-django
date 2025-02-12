from django.db import models
import re
from django.core.exceptions import ValidationError

def validate_cpf(value):
    """Ensure CPF has exactly 11 digits."""
    if not re.match(r'^\d{11}$', value):
        raise ValidationError("CPF must contain exactly 11 digits.")

class Customer(models.Model):
    customer_cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_created_at = models.DateTimeField(auto_now_add=True)
    customer_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.customer_name


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    house_number = models.CharField(max_length=20)
    complement = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.house_number} - {self.city}/{self.state}"
