from django.db import models

# Create your models here.
class CurrencyRate(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    courses = models.IntegerField(verbose_name='Текущий курс')
    date_of_update = models.DateField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return f"{self.name}:{self.courses}"


class CurrencyRateHistory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    courses = models.IntegerField(verbose_name='Текущий курс')
    timestamp = models.DateField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return f"{self.name}:{self.courses} at {self.timestamp}"