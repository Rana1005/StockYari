from rest_framework import serializers
from .models import IndexModel,DailyPriceModel

class DailyPriceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPriceModel
        fields = '__all__'

class IndexModelSerializer(serializers.ModelSerializer):
    daily_prices = DailyPriceModelSerializer(many=True, read_only=True)

    class Meta:
        model = IndexModel
        fields = '__all__'