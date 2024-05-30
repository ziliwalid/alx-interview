#!/usr/bin/python3
"""N-Queens solver"""

import sys

def is_safe(queen_shih, row, col):
    """Check if a position is safe for the queen."""
    for r, c in queen_shih:
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n):
    """Solve the N-Queens problem and return all possible solutions."""
    def backtrack(row):
        if row == n:
            solutions.append(queen_shih[:])
            return
        for col in range(n):
            if is_safe(queen_shih, row, col):
                queen_shih.append((row, col))
                backtrack(row + 1)
                queen_shih.pop()

    solutions = []
    queen_shih = []
    backtrack(0)
    return solutions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
