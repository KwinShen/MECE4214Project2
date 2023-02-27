import subprocess
import time
import os

with open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw") as f:
    while True:
        print(f.read())
        f.seek(0)
        time.sleep(1)
    f.close()