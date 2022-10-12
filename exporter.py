import prometheus_client
import psutil
import time
import shutil

UPDATE_PERIOD = 60
SYSTEM_USAGE = prometheus_client.Gauge('system_usage',
                                       'Hold current system resource usage',
                                       ['resource_type'])


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    prometheus_client.start_http_server(8000)
    # Generate some requests.
    while True:
        total1, used1, free1 = shutil.disk_usage("/mnt/disk1")
        SYSTEM_USAGE.labels('used1').set(used1)
        SYSTEM_USAGE.labels('free1').set(free1)
        total2, used2, free2 = shutil.disk_usage("/mnt/disk2")
        SYSTEM_USAGE.labels('used2').set(used2)
        SYSTEM_USAGE.labels('free2').set(free2)
        total3, used3, free3 = shutil.disk_usage("/mnt/disk3")
        SYSTEM_USAGE.labels('used3').set(used3)
        SYSTEM_USAGE.labels('free3').set(free3)
        total4, used4, free4 = shutil.disk_usage("/mnt/disk4")
        SYSTEM_USAGE.labels('used4').set(used4)
        SYSTEM_USAGE.labels('free4').set(free4)
        time.sleep(UPDATE_PERIOD)