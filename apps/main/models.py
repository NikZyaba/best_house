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


class SaveDbReview(models.Model):
    RATE_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]

    buyer_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True, default="")  # ИСПРАВЛЕНО
    description = models.TextField(max_length=1000)  # ИСПРАВЛЕНО: убрано unique=True
    rate = models.IntegerField(choices=RATE_CHOICES, default=5)  # ДОБАВЛЕН default

    def __str__(self):
        return f"{self.buyer_name} - {self.rate} звезд"

    class Meta:
        db_table = 'main_savedbreview'