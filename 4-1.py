import RPi.GPIO as GPIO

def dec2bin(val):
    return [int(n) for n in bin(val)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        n = input("Number: ")
        try:
            n = int(n)
            if 0 <= n <= 255:
                GPIO.output(dac, dec2bin(n))
                voltage = float(n) / 256.0 * 3.3
                print(f"Voltage: {voltage}")
            else:
                if n < 0:
                    print("Error, number < 0")
                elif n > 255:
                    print("Number more than 255")
        except Exception:
            if n == "q":
                break
            print("Error, its a string")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")