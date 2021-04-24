import time
from math import *
from displayStuff import plotSmall

X = True
O = False

RED = [255,0,0]
BLUE = [0,255,255]
BLACK = [0,0,0]

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

def plotDigit(pixels, image, pos, size, colour):
    for y in range(size[1]):
        for x in range(size[0]):
            xPos = pos[0]+x
            yPos = pos[1]+y
            #print(xPos,yPos)
            if image[y*size[0]+x]:
                pixels[yPos*8+xPos] = colour
            else:
                pixels[yPos*8+xPos] = BLACK
    return pixels


def displayNumber(pixels,number,pos,colour):
    number = addSpacers(number,2)
    pixels = plotDigit(pixels,images[int(number[0])],[pos[0]  ,pos[1]],[3,5],colour)
    pixels = plotDigit(pixels,images[int(number[1])],[pos[0]+4,pos[1]],[3,5],colour)
    return pixels

def digitalClock(pixels,screen):
    now = time.localtime()

    if screen == 1:
        pixels = displayNumber(pixels,now.tm_min,[1,2],BLUE)
    else:
        pixels = displayNumber(pixels,now.tm_hour,[0,1],RED)
    return pixels
    
    

def testDigitalClock():
    from sense_emu_pygame import SenseHat
    sense = SenseHat()
    for x in range(100):
        pixels = [[0,0,0] for x in range(64)]
        pixels = displayNumber(pixels,x,[0,1],RED)
        sense.set_pixels(pixels)
        time.sleep(.1)
        #input()

if __name__ == '__main__':
    testDigitalClock()
