#!/usr/bin/python3
"""
Module 0-nqueens
"""
import sys


def print_solutions(solutions):
    """ Prints the chess board """
    for solution in solutions:
        print(solution)


def is_safe(board, row, col, n, queens):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """ Function to actually solve the n queens """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row, queens):
        """ Function that implements backtracking """
        nonlocal solutions
        if row == n:
            solutions.append(queens[:])
            return

        for col in range(n):
            if is_safe(board, row, col, n, queens):
                board[row][col] = 1
                queens.append([row, col])
                backtrack(row + 1, queens)
                board[row][col] = 0
                queens.pop()

    backtrack(0, [])
    return solutions


def nqueens(n):
    """ Main program that solves the N queens problem. """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
