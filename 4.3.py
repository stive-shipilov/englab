import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

n = 10
k = GPIO.PWM(24, 5)
k.start(50)

try:
    while True:
        a = int(input())
        k.ChangeDutyCycle(a)
        print(3.3*a/100)
finally:
    k.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()
