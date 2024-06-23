#!/usr/bin/python3
"""determines the fewest number of coins needed"""


def makeChange(coins, total):
    """does stuff
    """
    if total <= 0:
        return 0

    else:
        item = sorted(coins)
        item.reverse()
        compteur = 0
        for coin in item:
            while(total >= coin):
                compteur += 1
                total -= coin
        if total == 0:
            return compteur
        return -1
