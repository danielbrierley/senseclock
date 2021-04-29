#!/usr/bin/env python
import time
from math import *
from weather import drawTemp
from displayStuff import displayNumber

#TODO
#1. Clean up and optimise drawLine()


YELLOW = [255,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
ORANGE = [255,127,0]
BLACK = [0,0,0]
RED = BLACK




def getInput(sense):
    global selected,run
    for event in sense.stick.get_events():
        #print("The joystick was {} {}".format(event.action, event.direction))
        if event.action == 'pressed':
            if event.direction == 'left':
                selected -= 1
                if selected < 0:
                    selected = limit
                #print(selected)
            if event.direction == 'right':
                selected += 1
                if selected > limit:
                    selected = 0
                #print(selected)
        if event.action == 'released':
            if event.direction == 'middle':
                run = False
                    
                    
                    
                    
def weatherSub(sense, weather):
    global run,selected,limit
    run = True
    selected = 0
    limit = 2
    while run:
        getInput(sense)
        
        pixels = [[0,0,0] for x in range(64)]

        if selected == 0: #Temperature
            pixels = drawTemp(pixels,weather)
        if selected == 1: #Humidity
            pixels = displayNumber(pixels,round(weather.get_humidity()),[1,1],[255,0,255])
        if selected == 2: #Pressure
            pixels = displayNumber(pixels,round(weather.get_pressure()),[1,1],[150,0,255])

        sense.set_pixels(pixels)
        
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass

        
        
        time.sleep(.01)
    
    

    
if __name__ == '__main__':
    weatherSub()
