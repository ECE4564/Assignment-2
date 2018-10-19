import RPi.GPIO as GPIO
import time

red = 16
green = 20
blue = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

class LED:
    def __init__(self, size):
        self.size = size

    def showVarieties(self):
        ones = int(self.size%10)
        tens = int((self.size%100 - ones)/10)
        hundreds = int((self.size - (ones + tens*10))/100)

        for i in range(hundreds):
            self.redBlink()

        for i in range(tens):
            self.greenBlink()

        for i in range(ones):
            self.blueBlink()


    def redBlink(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
        
        # Turn on red LED for half a second
        GPIO.output(red, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(red, GPIO.LOW)
        time.sleep(0.5)

    def greenBlink(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)

        # Turn on green LED for half a second
        GPIO.output(green, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(green, GPIO.LOW)
        time.sleep(0.5)

    def blueBlink(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)

        # Turn on blue LED for half a second
        GPIO.output(blue, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(blue, GPIO.LOW)
        time.sleep(0.5)
        
