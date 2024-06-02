from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class ContactMOdels(models.Model):
    full_name = models.CharField(max_length=250)
    reletionship = models.TextField(max_length=300)
    # phone_regax = RegexValidator(regex=r'^\+?1?\d{9,15}$',  message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regax],max_length=17)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField()
    address = models.CharField(max_length=240)

    def _str_(self):
        return self.full_name
