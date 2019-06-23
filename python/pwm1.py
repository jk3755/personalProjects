# use pwm to make an led fade bright and dim

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(False)


pwm = GPIO.PWM(12, 50)
pwm.start(0)

for i in range(100):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.1)

for i in range(100, 0, -1):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.1)
