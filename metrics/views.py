
from django.shortcuts import render
#from prometheus_client import multiprocess
#from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Counter
from prometheus_client import generate_latest
from prometheus_client import Counter

# Create your views here.
from django.http import HttpResponse
from prometheus_client import Info
from prometheus_client import CollectorRegistry

from metrics.service import c
from metrics.service import registry
def testingPageView(request):
    c.labels('200','GET', 'testing', 'v.0.1.0').inc()
    return HttpResponse('Hello, testing')


