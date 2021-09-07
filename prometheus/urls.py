# prometheus/urls.py
from django.urls import path
from .views import homePageView, metricsPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('metrics', metricsPageView, name='metrics')
]