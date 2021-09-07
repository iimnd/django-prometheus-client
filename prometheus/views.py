
from django.shortcuts import render
from django.http import HttpResponse
import random


# import fungsi untuk menampilkan data yang sudah di collect
from prometheus_client import generate_latest

#import fungsi counter, histgoram yang ada pada app metrics, file service,py
from metrics.service import c
from metrics.service import h
from metrics.service import registry

def homePageView(request):
    n = random.randint(0,22)
    # statement untuk counter, label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    c.labels('200','GET', 'home', 'v.0.1.0').inc()

    # statement untuk histogram, value yang akan di observe misalnya adalah n (random int) . label disesuaikan dengan variable counter yang sebelumnya sudah di definisikan ['code','method', 'path','version']
    h.labels('200','GET', 'home', 'v.0.1.0').observe(n)

    return HttpResponse('Hello, World!')


def metricsPageView(request):
    return HttpResponse(generate_latest(registry),content_type=str('text/plain; version=0.0.4; charset=utf-8'))


