# 8 Queens Problem using Backtracking

N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_queens(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queens(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False

def main():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_queens(board, 0):
        print("Solution does not exist")
        return

    print("One of the possible solutions:\n")
    print_board(board)

if __name__ == "__main__":
    main()