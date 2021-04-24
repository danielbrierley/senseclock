#!/usr/bin/env python
import time
from math import *
from sense_emu_pygame import SenseHat
from clock import drawClock, testClock
from digitalClock import digitalClock

#TODO
#1. Clean up and optimise drawLine()


YELLOW = [255,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
ORANGE = [255,127,0]
BLACK = [0,0,0]
RED = BLACK

selected = 0
limit = 1
screen = 0

def getInput():
    global selected
    for event in sense.stick.get_events():
        #print("The joystick was {} {}".format(event.action, event.direction))
        if event.action == 'pressed':
            if event.direction == 'left':
                selected -= 1
                if selected < 0:
                    selected = limit
                print(selected)
            if event.direction == 'right':
                selected += 1
                if selected > limit:
                    selected = 0
                print(selected)

def main():
    #now = time.localtime()
    #h,m = getClockAngles(now)
    #print(h)
    #print(m)

    while True:
        pixels = [[0,0,0] for x in range(64)]

        if selected == 0:
            pixels = drawClock(pixels)
        if selected == 1:
            pixels = digitalClock(pixels,screen)
            
        sense.set_pixels(pixels)
        
        getInput()
        
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass

        
        
        time.sleep(.01)
    
    

    
if __name__ == '__main__':
    sense = SenseHat()
    main()
