import RPi.GPIO as GPIO
import time

servo_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)



pwm.ChangeDutyCycle(8)
time.sleep(2)
pwm.ChangeDutyCycle(12)
time.sleep(2)
pwm.stop()
GPIO.cleanup()