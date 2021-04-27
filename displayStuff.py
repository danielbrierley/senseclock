import time
from math import *

RED = [255,0,0]
BLUE = [0,0,255]
BLACK = [0,0,0]

X = True
O = False

numbers = [
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
    O,O,X],
    [#Q
    O,X,O,
    O,O,X,
    O,X,O,
    O,O,O,
    O,X,O]]

def addSpacers(number, length, spacer='0'):
    number = str(number)
    while len(number) < length:
        number = spacer+number
    return number

def plotDigit(pixels, digit, pos, size, colour):
    digit = int(str(digit).replace('?','10'))
    image = numbers[digit]
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
    pixels = plotDigit(pixels,number[0],[pos[0]  ,pos[1]],[3,5],colour)
    pixels = plotDigit(pixels,number[1],[pos[0]+4,pos[1]],[3,5],colour)
    return pixels

def plotSmall(pixels, image, pos, size):
    for y in range(size[1]):
        for x in range(size[0]):
            xPos = pos[0]+x
            yPos = pos[1]+y
            #print(xPos,yPos)
            pixels[yPos*8+xPos] = image[y*size[0]+x]
    return pixels

