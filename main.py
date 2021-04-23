#!/usr/bin/env python
import time

now = time.localtime()

hour = ((now.tm_hour/12)-(now.tm_hour//12))*12

hourAngle = (hour/12)*360
minuteAngle = (now.tm_min/60)*360
print(hourAngle)
print(minuteAngle)
