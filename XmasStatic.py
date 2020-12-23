#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

gpio17 = 11
gpio05 = 29
gpio06 = 31
gpio07 = 26
gpio08 = 24
gpio09 = 21
gpio10 = 19
gpio11 = 23

pinList = [gpio17, gpio05, gpio06, gpio07, gpio08, gpio09, gpio10, gpio11]

for gpioPin in pinList:
    GPIO.setup(gpioPin, GPIO.OUT)
    GPIO.output(gpioPin, True)
