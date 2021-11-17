
from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime
from threading import Timer
from datetime import date





# import fungsi untuk menampilkan data yang sudah di collect
from prometheus_client import generate_latest

#import fungsi counter, histgoram yang ada pada app metrics, file service,py
from metrics.service import counter
from metrics.service import histogram
from metrics.service import gauge
from metrics.service import registry


x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def setup_version_everyday():
    today = date.today()
    d3 = today.strftime("%y.%m.%d")
    gauge.labels(d3).set(1)
    #...

t = Timer(secs, setup_version_everyday)
t.start()


def homePageView(request):
    random_number = random.randint(0,22)
    # statement untuk counter, label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    counter.labels('200','GET', 'home', 'internal').inc()
    

    # statement untuk histogram, value yang akan di observe misalnya adalah n (random int) . label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    histogram.labels('200','GET', 'home', 'internal').observe(random_number)

    return HttpResponse('Hello, World!')


def ovoPageView(request):
    random_number = random.randint(0,22)
    # statement untuk counter, label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    counter.labels('200','GET', '/ovo', 'ovo').inc()

    # statement untuk histogram, value yang akan di observe misalnya adalah n (random int) . label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    histogram.labels('200','GET', '/ovo', 'ovo').observe(random_number)
    

    return HttpResponse('Hello, OVO!')


def gopayPageView(request):
    random_number = random.randint(0,22)
    # statement untuk counter, label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    counter.labels('200','GET', '/gopay', 'gopay').inc()

    # statement untuk histogram, value yang akan di observe misalnya adalah n (random int) . label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    histogram.labels('200','GET', '/gopay', 'gopay').observe(random_number)

    return HttpResponse('Hello, GOPAY!')


def metricsPageView(request):
    return HttpResponse(generate_latest(registry),content_type=str('text/plain; version=0.0.4; charset=utf-8'))


