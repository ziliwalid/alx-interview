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

    if n == 1:
        return 0

    counter = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        counter += 1
    return counter
