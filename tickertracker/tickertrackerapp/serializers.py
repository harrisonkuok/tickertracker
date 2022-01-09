from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    ticker = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=256)
    mention = serializers.IntegerField(default=0, validators=[MaxValueValidator(9999)])
    price = serializers.DecimalField(default=0, max_digits=8, decimal_places=2)