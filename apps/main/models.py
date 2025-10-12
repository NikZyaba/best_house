from django.db import models

# Create your models here.
class SaveDbConsulting(models.Model):
    buyer_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000, unique=False)

    def __str__(self):
        return f"{self.buyer_name} - {self.phone_number}"

    class Meta:
        db_table = 'main_savedbconsulting'


class SaveDbCalculating(models.Model):
    buyer_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=50, unique=False)
    room_area = models.DecimalField(max_digits=20, decimal_places=2)
    company_name = models.CharField(max_length=50, unique=False)

    def __str(self):
        return f"{self.buyer_name} - {self.phone_number}"

    class Meta:
        db_table = 'main_savedbcalculating'
