import time
from math import *

def plotSmall(pixels, image, pos, size):
    for y in range(size[1]):
        for x in range(size[0]):
            xPos = pos[0]+x
            yPos = pos[1]+y
            #print(xPos,yPos)
            pixels[yPos*8+xPos] = image[y*size[0]+x]
    return pixels

