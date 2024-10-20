from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from serializers import ExchangerRatesSerializers, ExchangerRatesHistorySerializers
from models import CurrencyRate, CurrencyRateHistory


class RatesViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = ExchangerRatesSerializers



class RatesHistoryViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRateHistory.objects.all()
    serializer_class = ExchangerRatesHistorySerializers


    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        history = CurrencyRateHistory.objects.filter(name=pk).order_by('-timestamp')[:7]
        serializer = ExchangerRatesHistorySerializers(history, many=True)
        return Response(serializer.data)