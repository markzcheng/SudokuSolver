board = [
    [8, 0, 0, 9, 3, 0, 0, 0, 2],
    [0, 0, 9, 0, 0, 0, 0, 4, 0],
    [7, 0, 2, 1, 0, 0, 9, 6, 0],
    [2, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 7, 0, 0, 0, 6, 0, 0, 5],
    [0, 2, 7, 0, 0, 8, 4, 0, 6],
    [0, 3, 0, 0, 0, 0, 5, 0, 0],
    [5, 0, 0, 0, 6, 2, 0, 0, 8],
]

# function to print the sudoku board


def print_board(board):
    row = len(board)
    col = len(board[0])
    sep_length = 29

    for i in range(row):
        if i % 3 == 0 and i != 0:
            print(sep_length * "-")
        for j in range(col):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(board[i][j], end='  ')
        print()

# Find and return the row, col values of the first zero found
# Otherwise return None if there are no zeroes


def find_zero(board):
    # hello
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                return i, j
    return None

# Checks if the row, col, and square for a number is valid
# i refers to the row num and j refers to the col num


def valid_number(i, j, board):
    return valid_row(i, j, board) and valid_col(i, j, board) and valid_square(i, j, board)


def valid_row(i, j, board):
    val = board[i][j]
    for colNum in range(len(board[0])):
        if board[i][colNum] == val and (colNum != j):
            return False
    return True


def valid_col(i, j, board):
    val = board[i][j]
    for rowNum in range(len(board)):
        if board[rowNum][j] == val and (rowNum != i):
            return False
    return True


def valid_square(i, j, board):
    rowStart = (i // 3) * 3
    colStart = (j // 3) * 3
    val = board[i][j]
    for row in range(rowStart, rowStart + 3):
        for col in range(colStart, colStart + 3):
            if board[row][col] == val and (row != i or col != j):
                return False
    return True


def solve(board):

    coordinates = find_zero(board)
    if not coordinates:
        return True
    else:
        (row, col) = coordinates

    for i in range(1, 10):
        board[row][col] = i
        if valid_number(row, col, board):
            solved = solve(board)
            if solved:
                return True
        board[row][col] = 0

    return False


def run_program(board):
    print()
    print("The starting board looks like:\n")
    print_board(board)
    print()
    solved = solve(board)
    if solved:
        print("Solving...\n")
        print("The ending board looks like:\n")
        print_board(board)
    else:
        print("Invalid board. No solution exists.")
    print()


run_program(board)
