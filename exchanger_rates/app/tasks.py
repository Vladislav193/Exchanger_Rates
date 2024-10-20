import requests
from celery import shared_task
from models import CurrencyRate, CurrencyRateHistory


@shared_task
def update_currency_rates():
    url = "https://api.exchangeratesapi.io/latest?base=USD"
    response = requests.get(url=url)
    data = response.json()

    for name, rate in data["rates"].items():
        currency_rate, created = CurrencyRate.objects.update_or_create(
            currency=name,
            defaults={'rate': rate}
        )

        CurrencyRateHistory.objects.create(
            currency=name,
            rate=rate,
            timestamp=currency_rate.updated_at
        )