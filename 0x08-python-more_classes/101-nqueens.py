#!/usr/bin/python3
"""
N queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions
"""

import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens_util(board, col, N):
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen
            res = solve_queens_util(board, col + 1, N) or res  # Check next column
            board[i][col] = 0  # Backtrack if no solution found
    return res

def solve_queens(N):
    board = [[0] * N for _ in range(N)]  # Initialize the board
    if not solve_queens_util(board, 0, N):
        print("No solution exists")

def print_solution(board):
    N = len(board)
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)
