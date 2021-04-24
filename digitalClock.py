import time
from math import *
from displayStuff import plotSmall

X = [255,0,0]
O = [0,0,0]

images = [
    [#0
    X,X,X,
    X,O,X,
    X,O,X,
    X,O,X,
    X,X,X],
    [#1
    O,O,X,
    O,O,X,
    O,O,X,
    O,O,X,
    O,O,X],
    [#2
    X,X,X,
    O,O,X,
    X,X,X,
    X,O,O,
    X,X,X],
    [#3
    X,X,X,
    O,O,X,
    X,X,X,
    O,O,X,
    X,X,X],
    [#4
    X,O,X,
    X,O,X,
    X,X,X,
    O,O,X,
    O,O,X],
    [#5
    X,X,X,
    X,O,O,
    X,X,X,
    O,O,X,
    X,X,X],
    [#6
    X,X,X,
    X,O,O,
    X,X,X,
    X,O,X,
    X,X,X],
    [#7
    X,X,X,
    O,O,X,
    O,O,X,
    O,O,X,
    O,O,X],
    [#8
    X,X,X,
    X,O,X,
    X,X,X,
    X,O,X,
    X,X,X],
    [#9
    X,X,X,
    X,O,X,
    X,X,X,
    O,O,X,
    O,O,X]]

def addSpacers(number, length, spacer='0'):
    number = str(number)
    while len(number) < length:
        number = spacer+number
    return number

def displayNumber(pixels,number,pos):
    number = addSpacers(number,2)
    pixels = plotSmall(pixels,images[int(number[0])],[pos[0]  ,pos[1]],[3,5])
    pixels = plotSmall(pixels,images[int(number[1])],[pos[0]+4,pos[1]],[3,5])
    return pixels

def digitalClock(pixels,screen):
    now = time.localtime()

    if screen:
        pixels = displayNumber(pixels,now.tm_min,[0,1])
    else:
        pixels = displayNumber(pixels,now.tm_hour,[0,1])
    return pixels
    
    

def testDigitalClock():
    from sense_emu_pygame import SenseHat
    sense = SenseHat()
    for x in range(100):
        pixels = [[0,0,0] for x in range(64)]
        pixels = displayNumber(pixels,x,[0,1])
        sense.set_pixels(pixels)
        time.sleep(.1)
        #input()

if __name__ == '__main__':
    testDigitalClock()
