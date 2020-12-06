#!/usr/bin/env python

#
# This script is based on the script provided in the following instructable:
# https://www.instructables.com/Raspberry-Pi-Christmas-Tree-Light-Show/
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
time.sleep(2.0)

gpio4 = 7
GPIO.setup(gpio4, GPIO.OUT)
GPIO.output(gpio4, True)
time.sleep(2.0)
GPIO.output(gpio4, False)

gpio5 = 29
GPIO.setup(gpio5,  GPIO.OUT)
GPIO.output(gpio5, True)
time.sleep(2.0)
GPIO.output(gpio5, False)

gpio6 = 31
GPIO.setup(gpio6,  GPIO.OUT)
GPIO.output(gpio6, True)
time.sleep(2.0)
GPIO.output(gpio6, False)

gpio7 = 26
GPIO.setup(gpio7,  GPIO.OUT)
GPIO.output(gpio7, True)
time.sleep(2.0)
GPIO.output(gpio7, False)

gpio8 = 24
GPIO.setup(gpio8,  GPIO.OUT)
GPIO.output(gpio8, True)
time.sleep(2.0)
GPIO.output(gpio8, False)

gpio9 = 21
GPIO.setup(gpio9,  GPIO.OUT)
GPIO.output(gpio9, True)
time.sleep(2.0)
GPIO.output(gpio9, False)

gpio10 = 19
GPIO.setup(gpio10,  GPIO.OUT)
GPIO.output(gpio10, True)
time.sleep(2.0)
GPIO.output(gpio10, False)

gpio11 = 23
GPIO.setup(gpio11,  GPIO.OUT)
GPIO.output(gpio11, True)
time.sleep(2.0)
GPIO.output(gpio11, False)

