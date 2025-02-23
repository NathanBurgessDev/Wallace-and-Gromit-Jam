import RPI.GPIO as GPIO
import time

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
time.sleep(5)
GPIO.cleanup()
