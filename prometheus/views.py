
from django.shortcuts import render
from django.http import HttpResponse
import random


# import fungsi untuk menampilkan data yang sudah di collect
from prometheus_client import generate_latest

#import fungsi counter, histgoram yang ada pada app metrics, file service,py
from metrics.service import counter
from metrics.service import histogram
from metrics.service import registry

def homePageView(request):
    random_number = random.randint(0,22)
    # statement untuk counter, label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    counter.labels('200','GET', 'home', 'v.0.1.0').inc()

    # statement untuk histogram, value yang akan di observe misalnya adalah n (random int) . label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    histogram.labels('200','GET', 'home', 'v.0.1.0').observe(random_number)

    return HttpResponse('Hello, World!')


def metricsPageView(request):
    return HttpResponse(generate_latest(registry),content_type=str('text/plain; version=0.0.4; charset=utf-8'))


