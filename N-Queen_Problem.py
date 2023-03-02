def is_valid(board, row, col, n):
    """
    Checks if a queen can be placed at a given row and column on the board
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    """
    Recursive function that solves the N-Queens problem
    """
    if row == n:
        return True
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row+1, n):
                return True
            board[row][col] = 0
    return False

def print_board(board, n):
    """
    Prints the board in a readable format
    """
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

n = int(input("Enter the value of N: "))
board = [[0]*n for i in range(n)]

if solve_n_queens(board, 0, n):
    print("Found a solution:")
    print_board(board, n)
else:
    print("No solution exists for N = ", n)