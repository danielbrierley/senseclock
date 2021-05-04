#!/usr/bin/env python
import time
from math import *
from weather import drawTemp
from displayStuff import displayNumber, addSpacers

#TODO
#1. Clean up and optimise drawLine()


YELLOW = [255,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
ORANGE = [255,127,0]
BLACK = [0,0,0]
MAGENTA = [255,0,255]
PURPLE = [150,0,255]
RED = BLACK



def getInput(sense):
    global selected,run,screen
    for event in sense.stick.get_events():
        #print("The joystick was {} {}".format(event.action, event.direction))
        if event.action == 'pressed':
            if event.direction == 'left':
                selected -= 1
                if selected < 0:
                    selected = limit
                screen = 0
                #print(selected)
            if event.direction == 'right':
                selected += 1
                if selected > limit:
                    selected = 0
                screen = 0
                #print(selected)
        if event.action == 'released':
            if event.direction == 'middle':
                run = False
                    
                    
def showPressure(pixels, number, screen, colour):
    number = addSpacers(number, 4)
    if screen == 0:
        pixels = displayNumber(pixels,str(number)[:2],[0,1],colour)
        pixels[5*8+3] = ORANGE
        pixels[6*8+3] = ORANGE
    else:
        pixels = displayNumber(pixels,str(number)[2:4],[1,1],colour)
    return pixels
    
                    
def weatherSub(sense, weather):
    global run,selected,limit,screen
    run = True
    selected = 0
    limit = 2
    screen = 0
    maxScreen = 1
    prevSecs = [time.localtime().tm_sec+x for x in range(2)]
    prevMin = str(time.localtime().tm_min)[0]
    while run:
        getInput(sense)
        
        pixels = [[0,0,0] for x in range(64)]

        if selected == 0: #Temperature
            pixels = drawTemp(pixels,weather)
        if selected == 1: #Humidity
            pixels = displayNumber(pixels,round(weather.get_humidity()),[1,1],[255,0,255])
        if selected == 2: #Pressure
            pixels = showPressure(pixels, round(weather.get_pressure()),screen,[150,0,255])

        for x in range(8):
            pixels[7*8+x] = YELLOW

        sense.set_pixels(pixels)

        if not time.localtime().tm_sec in prevSecs:
            prevSecs = [time.localtime().tm_sec+x for x in range(2)]
            screen += 1
            if screen > maxScreen:
                screen = 0
                
        if not str(time.localtime().tm_min)[0] in prevMin and sense != weather:
            prevMin = str(time.localtime().tm_min)[0]
            weather.updateWeather(sense)
        
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass

        
        
        time.sleep(.01)
    
    

    
if __name__ == '__main__':
    weatherSub()
