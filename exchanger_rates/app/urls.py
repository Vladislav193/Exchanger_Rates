from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import RatesViewSet, RatesHistoryViewSet
app_name = 'api'

router = DefaultRouter()
router.register(r'rates', RatesViewSet, basename='rates')
router.register(r'rates-history', RatesHistoryViewSet, basename='rates-history')

urlpatterns = [
    path('api/', include(router.urls) )
]