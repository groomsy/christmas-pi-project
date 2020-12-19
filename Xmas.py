#!/usr/bin/env python

#
# Command Line usage:
#   Xmas.py <input sequence> <audio file>
#
# This script is based on the script provided in the following instructable:
# https://www.instructables.com/Raspberry-Pi-Christmas-Tree-Light-Show/
#

from typing import List

import RPi.GPIO as GPIO
import pygame
import sys
import time


def convert_seconds_to_ms(seconds):
    return int(round(seconds * 1000))


#
# GPIO Map
#
gpio17 = 11
gpio05 = 29
gpio06 = 31
gpio07 = 26
gpio08 = 24
gpio09 = 21
gpio10 = 19
gpio11 = 23

#
# Section-to-Pin Map
# Sections 1-5 will be light banding (1 at top of tree, 5 at bottom)
# Section 6 will be Red lights
# Section 7 will be Green lights
# Section 8 will be Blue lights
#
sectionToPinMap = {
    1: gpio17,
    2: gpio05,
    3: gpio06,
    4: gpio07,
    5: gpio08,
    6: gpio09,
    7: gpio10,
    8: gpio11
}

#
# Setup the board
#
GPIO.setmode(GPIO.BOARD)
for section, gpioPin in sectionToPinMap.items():
    print(f'Setting up {gpioPin} for {section}.')
    GPIO.setup(gpioPin, GPIO.OUT)
    GPIO.output(gpioPin, False)

print(f'Let system settle.')
time.sleep(2.0)

#
# Load sequence file
#
sequenceFile = sys.argv[1]
print(f'Open sequence file ({sequenceFile}) and parse.')
with open(sequenceFile, 'r') as f:
    sequenceData: List[str] = f.readlines()
    for i in range(len(sequenceData)):
        sequenceData[i] = sequenceData[i].rstrip()

#
# Load and play the music
#
musicFile = sys.argv[2]
print(f'Starting playback of {musicFile}.')
pygame.mixer.init()
pygame.mixer.music.load(musicFile)
pygame.mixer.music.play()

# Start sequencing
startTime = convert_seconds_to_ms(time.time())
step = 1  # Ignore the header line
while True:
    nextStep = sequenceData[step].split(",")
    nextStep[1] = nextStep[1].rstrip()
    currentTime = convert_seconds_to_ms(time.time()) - startTime

    nextStepTimeInMS = nextStep[0]
    if int(nextStepTimeInMS) <= currentTime:
        print(f'Running next step.')

        command: str = nextStep[1].rstrip()
        if "1" <= command <= "8":
            # If command is 1-8, then we'll update the section with the specified state.
            state = False
            if nextStep[2] == "1":
                state = True

            print(f'Update section {command} to {state}.')
            section = int(command)
            GPIO.output(sectionToPinMap[section], state)

        # if the END command
        if command == "END":
            print(f'Reached END; set all pins to False.')
            for section, gpioPin in sectionToPinMap.items():
                GPIO.output(gpioPin, False)
            break
        step += 1
