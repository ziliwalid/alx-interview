#!/usr/bin/python3
"""queens"""


import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    sol = []
    queen_shih = []
    stop = False
    ro = 0
    col = 0

    while ro < n:
        goback = False
        while col < n:
            safe = True
            for cord in queen_shih:
                col_check = cord[1]
                if(col_check == col or col_check + (ro-cord[0]) == col or
                        col_check - (ro-cord[0]) == col):
                    safe = False
                    break

            if not safe:
                if col == n - 1:
                    goback = True
                    break
                col += 1
                continue

            cords = [ro, col]
            queen_shih.append(cords)
            if ro == n - 1:
                sol.append(queen_shih[:])
                for cord in queen_shih:
                    if cord[1] < n - 1:
                        ro = cord[0]
                        col = cord[1]
                for i in range(n - ro):
                    queen_shih.pop()
                if ro == n - 1 and col == n - 1:
                    queen_shih = []
                    stop = True
                ro -= 1
                col += 1
            else:
                col = 0
            break
        if stop:
            break
        if goback:
            ro -= 1
            while ro >= 0:
                col = queen_shih[ro][1] + 1
                del queen_shih[ro]
                if col < n:
                    break
                ro -= 1
            if ro < 0:
                break
            continue
        ro += 1

    for idx, val in enumerate(sol):
        if idx == len(sol) - 1:
            print(val, end='')
        else:
            print(val)