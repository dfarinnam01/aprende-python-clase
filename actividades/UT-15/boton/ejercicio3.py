import RPi.GPIO as GPIO
import time

led = 11
boton = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

estado_led = False
ultimo_estado_boton = GPIO.input(boton)

while True:
    estado_boton = GPIO.input(boton)
    if ultimo_estado_boton == GPIO.HIGH and estado_boton == GPIO.LOW:
        estado_led = not estado_led
        GPIO.output(led, estado_led)

    ultimo_estado_boton = estado_boton
    time.sleep(0.05)
