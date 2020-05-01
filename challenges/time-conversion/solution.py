#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour   = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    ampm = s[8:10]
    if (ampm.upper() == "PM") and (hour != "12"):
        hour = int(hour) + 12
    if hour == 24 or (ampm.upper() == "AM" and hour == "12"):
        shour = "00"
    else:
        shour = str(hour)
    return shour + ":" + minute + ":" + second
    print ([hour,minute,second, ampm])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
