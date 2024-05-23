#!/usr/bin/python3
"""utf 8"""


def validUTF8(data):
    """validates utf 8
    through an algorithm
    """
    nb = 0 ###number bytes###

    param1 = 1 << 7
    param2 = 1 << 6

    for i in data:

        mb = 1 << 7

        if nb == 0:

            while mb & i:
                nb += 1
                mb = mb >> 1

            if nb == 0:
                continue

            if nb == 1 or nb > 4:
                return False

        else:
            if not (i & param1 and not (i & param2)):
                return False

        nb -= 1

    if nb == 0:
        return True

    return False
