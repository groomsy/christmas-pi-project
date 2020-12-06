#!/usr/bin/env python

#
# This script is based on the script provided in the following instructable:
# https://www.instructables.com/Raspberry-Pi-Christmas-Tree-Light-Show/
#

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

gpio4 = 7
gpio5 = 29
gpio6 = 31
gpio7 = 26
gpio8 = 24
gpio9 = 21
gpio10 = 19
gpio11 = 23

pinList = [gpio4, gpio5, gpio6, gpio7, gpio8, gpio9, gpio10, gpio11]

for gpioPin in pinList:
    GPIO.setup(gpioPin, GPIO.OUT)
    GPIO.output(gpioPin, False)

time.sleep(2.0)

for gpioPin in pinList:
    GPIO.output(gpioPin, True)
    time.sleep(2.0)
    GPIO.output(gpioPin, False)