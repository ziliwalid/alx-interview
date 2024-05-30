#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.
"""
import sys

def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)

def print_error_and_exit(message):
    """Print an error message and exit with status 1."""
    print(message)
    sys.exit(1)

def is_valid(board, row, col):
    """
    Check if placing a queen at (row, col) is valid.
    
    Args:
        board (list): The current board configuration.
        row (int): The row index.
        col (int): The column index.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """
    Solve the N-queens problem and return all solutions.
    
    Args:
        N (int): The size of the chessboard.
    
    Returns:
        list: A list of solutions, each solution is a list of column indices.
    """
    def solve(row, board):
        """
        Recursively attempt to place queens on the board.
        
        Args:
            row (int): The current row to place a queen.
            board (list): The current board configuration.
        """
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(0, board)
    return solutions

def main():
    """Main function to parse arguments and solve the N-queens problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")
    
    if N < 4:
        print_error_and_exit("N must be at least 4")
    
    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

if __name__ == "__main__":
    main()

