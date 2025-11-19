import RPi.GPIO as GPIO
import time

led = 11
boton = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

UMBRAL = 1.0
while True:
    while GPIO.input(boton) == GPIO.HIGH:
        time.sleep(0.01)

    inicio = time.time()
    GPIO.output(led, GPIO.HIGH)
    
    while GPIO.input(boton) == GPIO.LOW:
        time.sleep(0.01)

    fin = time.time()
    GPIO.output(led, GPIO.LOW)

    duracion = fin - inicio
    if duracion < UMBRAL:
        print("pulso corto")
    else:
        print("pulso largo")
