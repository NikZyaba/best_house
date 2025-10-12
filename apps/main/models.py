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


# models.py
class SaveDbCalculating(models.Model):
    buyer_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    room_area = models.FloatField(default=10.0)  # Явное default значение
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'main_savedbcalculating'

    def __str__(self):
        return f"{self.buyer_name} - {self.room_type} ({self.room_area}m²)"
