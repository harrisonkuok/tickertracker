from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=256)
    mention = models.IntegerField(default=0, validators=[MaxValueValidator(9999)])
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def get_top_mentioned(number):
        return Stock.objects.order_by('-mention')[:number]

    def __str__(self):
        return self.ticker
