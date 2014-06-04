#!/usr/bin/env python

# This program goes on the Raspberry Pi

from RPi.GPIO import *
from time import sleep
import MCtoPi

setmode(BCM)

SIG = 17

setup(SIG, IN)

class Door(MCtoPi.MCtoPi):
    def get(self, output, input):
        output.write(input(SIG))

if __name__ == '__main__':
    print 'Serving on port 3141'
    try:
        MCtoPi.start(Door, 3141)
    except KeyboardInterrupt:
        pass
    cleanup()
    print('\nBye!')
