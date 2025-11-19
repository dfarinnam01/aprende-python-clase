import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 7
LED2 = 11
LED3 = 13
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

GPIO.output(LED, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.output(LED3, GPIO.LOW)
while True:
    GPIO.output(LED3, GPIO.HIGH)
    time.sleep(8)
    GPIO.output(LED3, GPIO.LOW)
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(2)
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(8)
    GPIO.output(LED, GPIO.LOW)
