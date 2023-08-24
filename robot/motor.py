import RPi.GPIO as GPIO
import time

class Robot:
    def __init__(self):
        self.M1a = 11
        self.M1b = 12
        self.M2a = 15
        self.M2b = 16
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.M1a, GPIO.OUT)
        GPIO.setup(self.M1b, GPIO.OUT)
        GPIO.setup(self.M2a, GPIO.OUT)
        GPIO.setup(self.M2b, GPIO.OUT)

    def forward(self):
        GPIO.output(self.M1a, GPIO.HIGH)
        GPIO.output(self.M1b, GPIO.LOW)
        GPIO.output(self.M2a, GPIO.HIGH)
        GPIO.output(self.M2b, GPIO.LOW)

    def backward(self):
        GPIO.output(self.M1a, GPIO.LOW)
        GPIO.output(self.M1b, GPIO.HIGH)
        GPIO.output(self.M2a, GPIO.LOW)
        GPIO.output(self.M2b, GPIO.HIGH)

    def left(self):
        GPIO.output(self.M1a, GPIO.LOW)
        GPIO.output(self.M1b, GPIO.HIGH)
        GPIO.output(self.M2a, GPIO.HIGH)
        GPIO.output(self.M2b, GPIO.LOW)


    def right(self):
        GPIO.output(self.M1a, GPIO.HIGH)
        GPIO.output(self.M1b, GPIO.LOW)
        GPIO.output(self.M2a, GPIO.LOW)
        GPIO.output(self.M2b, GPIO.HIGH)


    def stop(self):
        GPIO.output(self.M1a, GPIO.LOW)
        GPIO.output(self.M1b, GPIO.LOW)
        GPIO.output(self.M2a, GPIO.LOW)
        GPIO.output(self.M2b, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()
