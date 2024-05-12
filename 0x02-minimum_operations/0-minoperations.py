#!/usr/bin/python3

"""
    function determines the number of minmum operations given an n
"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to give a result of exactly n H characters in a file
    args: n: Number of characters to be displayed
    return: number of min operations
    """
    
    current = 1
    start = 0
    cou = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            start = current
            current += start
            cou += 2
        else:
            current += start
            cou += 1
    return cou
