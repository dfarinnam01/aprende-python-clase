import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
boton=7
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
        boton_estado = GPIO.input(boton)
        print(boton_estado)
        time.sleep(0.5)




