#!/usr/bin/python3
"""
N-Queens Solver

This program solves the N-Queens problem and prints the solutions.
"""

import sys

def is_safe(board, row, col, N):
    """Check if placing a queen at position (row, col) is safe."""
    # Check if there's a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col, N):
    """Recursively solve the N-Queens problem."""
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_queens(board, col + 1, N) or res
            board[i][col] = 0

    return res

def print_solution(board):
    """Print the coordinates of queens in the solution."""
    N = len(board)
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)
