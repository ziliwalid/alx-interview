#!/usr/bin/python3

"""reads stdin lines"""

import sys


def printStats(dic, size):
    """ prints stats"""
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

countStat = 0
length = 0

try:
    for line in sys.stdin:
        if countStat != 0 and countStat % 10 == 0:
            printStats(stats, length)

        stlist = line.split()
        countStat += 1

        try:
            length += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in stats:
                stats[stlist[-2]] += 1
        except:
            pass
    printStats(stats, length)

except KeyboardInterrupt:
    printStats(stats, length)
    raise
