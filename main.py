#!/usr/bin/env python
import time

def angleSimplify(angle):
    while angle >= 360:
        angle -= 360
    while angle < 0:
        angle += 360
    return angle

now = time.localtime()

hourAnglePerc = now.tm_hour/12
minuteAnglePerc = now.tm_min/60

hourAngle = hourAnglePerc*360
minuteAngle = minuteAnglePerc*360

hourAngle += minuteAnglePerc*(360/12)

print(angleSimplify(hourAngle))
print(angleSimplify(minuteAngle))
