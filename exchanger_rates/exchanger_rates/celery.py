from celery import Celery


app = Celery('currency_tracker',
             broker='redis://localhost:6379/0')
app.conf.beat_schedule = {
    'update_currency_rates':{
        'task': 'currency.tasks.update_currency_rates',
        'schedule': 1800.0,
    }
}