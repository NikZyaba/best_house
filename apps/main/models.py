from django.db import models

# Create your models here.
class SaveDb(models.Model):
    buyer_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=50, unique=False)
    description = models.CharField(max_length=1000, unique=False)

    def __str__(self):
        return f"{self.buyer_name} - {self.phone_number}"
