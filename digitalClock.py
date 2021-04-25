import time
from math import *
from displayStuff import displayNumber


RED = [255,0,0]
BLUE = [0,0,255]
BLACK = [0,0,0]



def digitalClock(pixels,screen):
    now = time.localtime()

    DOT1 = 2
    DOT2 = 4
    if screen == 1:
        pixels = displayNumber(pixels,now.tm_min,[1,1],BLUE)
        pixels[DOT1*8] = [0,255,0]
        pixels[DOT2*8] = [0,255,0]
    else:
        pixels = displayNumber(pixels,now.tm_hour,[0,1],RED)
        pixels[DOT1*8+7] = [0,255,0]
        pixels[DOT2*8+7] = [0,255,0]
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
