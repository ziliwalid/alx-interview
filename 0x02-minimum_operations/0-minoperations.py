#!/usr/bin/python3

"""
    function determines the number of minmum operations given an n
"""


def minOperations(n):
    """
    Calculates the minimum number of operations required to
    obtain exactly n 'H' characters.
    Args:
        n (int): The number of 'H' characters to be obtained.
    Returns:
        int: The minimum number of operations required.
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
