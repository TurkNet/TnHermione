from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter('request_count', 'Total number of requests received', ['endpoint', 'method', 'status_code'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])
