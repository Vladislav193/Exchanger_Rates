from rest_framework import serializers
from models import CurrencyRate, CurrencyRateHistory


class ExchangerRatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ['name', 'courses', 'date_of_update']


class ExchangerRatesHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRateHistory
        fields = ['name', 'courses', 'timestamp']