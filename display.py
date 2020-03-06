import RPi.GPIO as GPIO
import time
import subprocess

PIN = 4
TIMEON_SEC = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)


def set_display_power(power):
    arg = "1" if power else "0"
    subprocess.call(["vcgencmd", "display_power", arg])


while True:
    if GPIO.input(PIN) == 1:
        print("sensor an")
        set_display_power(False)
        time.sleep(TIMEON_SEC)
        set_display_power(True)
        print("done")
    else:
        print("sensor aus")
