import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

PIN_LED = 7
GPIO.setup(PIN_LED, GPIO.OUT)

LED_PWM = GPIO.PWM(PIN_LED, 100)
LED_PWM.start(0)

while True:
    for i in range(100):
        LED_PWM.ChangeDutyCycle(i)
        time.sleep(0.02)
    for i in range(100,0,-1):
        LED_PWM.ChangeDutyCycle(i)
        time.sleep(0.02)