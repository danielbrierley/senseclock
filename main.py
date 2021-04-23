#!/usr/bin/env python
import time
from math import *
from sense_emu_pygame import SenseHat

#TODO
#1. Clean up and optimise drawLine()


YELLOW = [255,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
ORANGE = [255,127,0]

def angleSimplify(angle):
    while angle >= 360:
        angle -= 360
    while angle < 0:
        angle += 360
    return angle

def getClockAngles(now):
    hourAnglePerc = now.tm_hour/12
    minuteAnglePerc = now.tm_min/60

    hourAngle = hourAnglePerc*360
    minuteAngle = minuteAnglePerc*360

    hourAngle += minuteAnglePerc*(360/12)

    hourAngle = angleSimplify(hourAngle)
    minuteAngle = angleSimplify(minuteAngle)

    return hourAngle, minuteAngle

def drawLine(pixels, colour, width, angle, bounds=[range(1,8),range(7)]):
    start = (4,3)
    angle = round(angleSimplify(angle))
    #width = 3
    if angle in range(45):
        t = tan(radians(angle))
    elif angle in range(45,90):
        t = tan(radians(90-angle))
        
    elif angle in range(90,90+45):
        t = tan(radians(angle-90))
    elif angle in range(90+45,180):
        t = tan(radians(90-angle-90))
        
    elif angle in range(180,180+45):
        t = tan(radians(angle-180))
    elif angle in range(180+45,270):
        t = tan(radians(180-angle-90))
        
    elif angle in range(270,270+45):
        t = tan(radians(angle-270))
    elif angle in range(270+45,360):
        t = tan(radians(360-angle))
        
    a = width
    for i in range(a):
        #0-90
        if angle in range(45):
            x = start[0]+round(t*i)
            y = start[1]-i
        elif angle in range(45,90):
            x = start[0]+i
            y = start[1]-round(t*i)
        #90-180
        elif angle in range(90,90+45):
            x = start[0]+i
            y = start[1]+round(t*i)
        elif angle in range(90+45,180):
            x = start[0]+round(t*i)
            y = start[1]+i
        #180-270
        elif angle in range(180,180+45):
            x = start[0]-round(t*i)
            y = start[1]+i
        elif angle in range(180+45,270):
            x = start[0]-i
            y = start[1]+round(t*i)
        #270-360
        elif angle in range(270,270+45):
            x = start[0]-i
            y = start[1]-round(t*i)
        elif angle in range(270+45,360):
            x = start[0]-round(t*i)
            y = start[1]-i
        #print(y)
        try:
            #if x in bounds[0] and y in bounds[1]:
            try:
                pixels[(y*8)+x] = colour
            except UnboundLocalError:
                print(angle)
        except IndexError:
            pass
    return pixels
        
    

def main():
    #now = time.localtime()
    #h,m = getClockAngles(now)
    #print(h)
    #print(m)

    sense = SenseHat()
##    for x in range(0,360):
##        pixels = [[0,0,0] for x in range(64)]
##        for y in range(8):
##            pixels[y*8] = RED
##        for x2 in range(8):
##            pixels[(y*8)+x2] = RED
##        pixels = drawLine(pixels, BLUE, 3, x+90)
##        pixels = drawLine(pixels, YELLOW, 4, x)
##        sense.set_pixels(pixels)
##        time.sleep(0.01)
    while True:
        pixels = [[0,0,0] for x in range(64)]
        for y in range(8):
            pixels[y*8] = RED
        for x2 in range(8):
            pixels[(y*8)+x2] = RED
            
        now = time.localtime()
        h,m = getClockAngles(now)
        pixels = drawLine(pixels, BLUE, 3, h)
        pixels = drawLine(pixels, YELLOW, 4, m)
        
        pixels[(3*8)+4] = ORANGE
        
        sense.set_pixels(pixels)
        sense.mainloop()
        time.sleep(.1)
    
    

    
if __name__ == '__main__':
    main()
