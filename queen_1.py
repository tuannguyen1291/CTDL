def can_place(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if can_place(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1

    return False

def print_board(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "1 "
            else:
                line += "0 "
        print(line)
    print()

n=int(input("Nhập vào kích cỡ bàn phím: "))
board = [-1] * n
solve(board, 0)
print_board(board)
