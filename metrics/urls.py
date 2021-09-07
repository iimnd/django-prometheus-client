# metrics/urls.py
from django.urls import path
from .views import testingPageView

urlpatterns = [
    path('testing', testingPageView, name='testing')
]