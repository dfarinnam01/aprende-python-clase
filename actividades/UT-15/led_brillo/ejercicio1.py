import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

PIN_LED = 7
GPIO.setup(PIN_LED, GPIO.OUT)

LED_PWM = GPIO.PWM(PIN_LED, 1)
LED_PWM.start(0)


while True:
    LED_PWM.ChangeDutyCycle(100)
    time.sleep(0.5)
    LED_PWM.ChangeDutyCycle(0)
    time.sleep(0.5)
