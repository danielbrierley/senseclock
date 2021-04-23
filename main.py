#!/usr/bin/env python
import time
from sense_emu_pygame import SenseHat

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

def main():
    now = time.localtime()
    h,m = getClockAngles(now)
    print(h)
    print(m)

    #sense = SenseHat()

    
if __name__ == '__main__':
    main()
