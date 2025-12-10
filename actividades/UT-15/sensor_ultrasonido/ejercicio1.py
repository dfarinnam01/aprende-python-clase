import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
TRIG = 8
ECHO = 10
while True:
    print ("Midiendo …")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    # Esperamos que el sensor se estabilice
    time.sleep(2)
    # Activamos el disparador enviando un pulso de 10 microsegundos
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    # Esperamos que se active el pin ECHO
    while GPIO.input(ECHO)==0:
        pulso_ini = time.time()
    while GPIO.input(ECHO)==1:
        pulso_fin = time.time()
    #Calculamos la duración del pulso
    pulso_duracion = pulso_fin - pulso_ini

    distancia = pulso_duracion * 17150
    distancia = round(distancia, 2)
    print (f"Distancia medida: {distancia} cm")
    GPIO.cleanup()