# prometheus/urls.py
from django.urls import path
from .views import homePageView, metricsPageView, ovoPageView, gopayPageView

urlpatterns = [
    path('ovo', ovoPageView, name='ovo'),
    path('gopay', gopayPageView, name='gopay'),
    path('metrics', metricsPageView, name='metrics')
]