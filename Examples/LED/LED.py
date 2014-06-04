#!/usr/bin/env python

# This program goes on the Raspberry Pi

from RPi.GPIO import *
from time import sleep
import MCtoPi

setmode(BCM)

SIG = 23

setup(SIG, OUT)

class LED(MCtoPi.MCtoPi):
    def get(self, _output, _input):
        output(SIG, _input)

if __name__ == '__main__':
    print 'Serving on port 3141'
    try:
        MCtoPi.start(LED, 3141)
    except KeyboardInterrupt:
        pass
    cleanup()
    print('\nBye!')
