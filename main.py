#!/usr/bin/env python
import time
from math import *
try:
    from sense_hat import SenseHat
except:
    from sense_emu_pygame import SenseHat
from clock import drawClock, testClock
from digitalClock import digitalClock
from weather import Weather, drawTemp
from game import Game
from input import textInput

#TODO
#1. Clean up and optimise drawLine()


YELLOW = [255,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
ORANGE = [255,127,0]
BLACK = [0,0,0]
RED = BLACK

sense = SenseHat()

game = sense.load_image('images/game.png', redraw=False)
pin = sense.load_image('images/pin.png', redraw=False)

selected = 0
limit = 6

def getInput(sense,weather):
    global selected, screen, prevSecs
    for event in sense.stick.get_events():
        #print("The joystick was {} {}".format(event.action, event.direction))
        if event.action == 'pressed':
            if event.direction == 'left':
                selected -= 1
                if selected < 0:
                    selected = limit
                screen = 0
                prevSecs = [time.localtime().tm_sec+x for x in range(2)]
                #print(selected)
            if event.direction == 'right':
                selected += 1
                if selected > limit:
                    selected = 0
                screen = 0
                prevSecs = [time.localtime().tm_sec+x for x in range(2)]
                #print(selected)
        if event.action == 'released':
            if event.direction == 'middle':
                if selected == 5:
                    #print('game')
                    Game(sense)
                if selected == 6:
                    sense.show_message('Set Location')
                    sense.stick.get_events()
                    loc = textInput(sense)
                    if loc:
                        weather.updateLocation(loc,sense)
                    sense.show_message(loc)
                    
                    
                    
                    
def main():
    global screen, maxScreen, prevSecs
    #now = time.localtime()
    #h,m = getClockAngles(now)
    #print(h)
    #print(m)
    screen = 0
    maxScreen = 1
    prevSecs = [time.localtime().tm_sec+x for x in range(2)]
    prevMin = str(time.localtime().tm_min)[0]
    weather = Weather(sense)

    while True:
        getInput(sense,weather)
        
        pixels = [[0,0,0] for x in range(64)]

        if selected == 0:
            pixels = drawClock(pixels)
        if selected == 1:
            pixels = digitalClock(pixels,screen)
        if selected == 2:
            pixels = drawTemp(pixels,weather)
        if selected == 3:
            pixels = weather.icon
        if selected == 4:
            pixels = drawTemp(pixels,sense)
        if selected == 5:
            pixels = game
        if selected == 6:
            pixels = pin

        sense.set_pixels(pixels)

        if not time.localtime().tm_sec in prevSecs:
            prevSecs = [time.localtime().tm_sec+x for x in range(2)]
            screen += 1
            if screen > maxScreen:
                screen = 0
                
        if not str(time.localtime().tm_min)[0] in prevMin:
            prevMin = str(time.localtime().tm_min)[0]
            weather.updateWeather(sense)
        
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass

        
        
        time.sleep(.01)
    
    

    
if __name__ == '__main__':
    main()
