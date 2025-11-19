import RPi.GPIO as GPIO
import time

led = 11
boton=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(boton) == GPIO.HIGH:
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)
    time.sleep(0.05)