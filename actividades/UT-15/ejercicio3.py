import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 7
LED2 = 11
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
while True:
        GPIO.output(LED, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(1)

        GPIO.output(LED, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(1)