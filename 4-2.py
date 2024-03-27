import RPi.GPIO as GPIO
from time import sleep

def dec2bin(val):
    return [int(n) for n in bin(val)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

flag = 1
a = 0
b = 0

try:
    period = float(input("Write period "))
    while True:
        GPIO.output(dac, dec2bin(b))
        if b == 0:
            flag = 1
        elif a == 255:
            flag = 0

        if flag == 1:
            b = b + 1
        else:
            b = b - 1
        
        sleep(period/10)

        a += 1
except ValueError:
    print("Its not a period")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")