N = 4

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens(board, col):
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0  # Backtrack

    return res

board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_n_queens(board, 0):
    print("Solution does not exist")
