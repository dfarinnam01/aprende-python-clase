import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED=7
GPIO.setup(LED,GPIO.OUT)
estado=GPIO.input(LED)
if estado== GPIO.HIGH:
        GPIO.output(LED,GPIO.LOW)
else:
        GPIO.output(LED,GPIO.HIGH)