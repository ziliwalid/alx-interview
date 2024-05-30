#!/usr/bin/python3
"""Solves the N-queens puzzle.
Finds all possible solutions to placing N
non-attacking queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    chessboard (list): A list of lists representing the chessboard.
    all_solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def create_board(size):
    """Create an `size`x`size` chessboard initialized with spaces."""
    board = []
    [board.append([]) for _ in range(size)]
    [row.append(' ') for _ in range(size) for row in board]
    return board


def deepcopy_board(board):
    """Return a deep copy of a chessboard."""
    if isinstance(board, list):
        return list(map(deepcopy_board, board))
    return board


def extract_solution(board):
    """Extract the solution from a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_attacks(board, row, col):
    """Mark all squares where queens can attack on the chessboard.
    Args:
        board (list): The current chessboard.
        row (int): The row of the last placed queen.
        col (int): The column of the last placed queen.
    """
    # Mark all squares to the right
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all squares to the left
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all squares below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all squares above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all squares diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all squares diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # Mark all squares diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all squares diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_nqueens(board, row, queens, solutions):
    """Recursively solve the N-queens problem.
    Args:
        board (list): The current chessboard.
        row (int): The current row to place a queen.
        queens (int): The current number of placed queens.
        solutions (list): A list of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(extract_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            temp_board = deepcopy_board(board)
            temp_board[row][col] = "Q"
            mark_attacks(temp_board, row, col)
            solutions = solve_nqueens(temp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(int(sys.argv[1]))
    solutions = solve_nqueens(board, 0, 0, [])
    for sol in solutions:
        print(sol)

