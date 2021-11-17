

# import type metrics dan collector registry prometheus client
from prometheus_client import Info
from prometheus_client import CollectorRegistry
from prometheus_client import Histogram
from prometheus_client import Counter
from prometheus_client import Gauge

#mendefinisikan registry, registry disini berfungsi untuk collector
registry = CollectorRegistry()

# mendifinisikan bucket, bucket adalah batasan persebaran data (yang dipakai oleh prometheus adalah lest equals)
buckets = [100,300,500,700,1000, 1200]

#mendifinisikan metrics, serta meregister metris pada registry sebelumnya
counter = Counter('request_counter', 'http request counter', ['code','method', 'path','partner'],registry=registry)
histogram = Histogram('process_time', 'processing time', ['code','method', 'path','partner'],registry=registry, buckets=buckets)
gauge = Gauge('my_custom_app_version', 'versioning app', ['version'],registry=registry)
info = Info('process_info', 'processing info', ['code','method', 'path','partner'],registry=registry)


#gauge.labels('v.0.1.0').set(1)