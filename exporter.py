import prometheus_client
import psutil
import time
import shutil

UPDATE_PERIOD = 3
SYSTEM_USAGE = prometheus_client.Gauge('system_usage',
                                       'Hold current system resource usage',
                                       ['resource_type'])


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    prometheus_client.start_http_server(8000)
    # Generate some requests.
    while True:
        total, used, free = shutil.disk_usage("/")
        SYSTEM_USAGE.labels('used').set(used)
        SYSTEM_USAGE.labels('free').set(free)
        time.sleep(UPDATE_PERIOD)
        SYSTEM_USAGE.labels('cpu_load').set(psutil.getloadavg()[0])