def is_valid(board, row, col):
    # Kiểm tra hàng
    for i in range(len(board)):
        if board[row][i] == 1:
            return False

    # Kiểm tra cột
    for i in range(len(board)):
        if board[i][col] == 1:
            return False

    # Kiểm tra đường chéo chính
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Kiểm tra đường chéo phụ
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve(board, row):
    # Nếu đã xử lý hết các hàng, trả về True và kết thúc thuật toán
    if row == len(board):
        return True

    # Duyệt từng ô trong hàng hiện tại
    for col in range(len(board)):
        # Nếu ô hiện tại hợp lệ, đặt quân hậu vào vị trí đó
        if is_valid(board, row, col):
            board[row][col] = 1

            # Tiếp tục xử lý cho hàng tiếp theo
            if solve(board, row + 1):
                return True

            # Nếu không tìm được giải pháp, quay lại vị trí trước đó và thử với vị trí khác
            board[row][col] = 0

    # Nếu không thể đặt quân hậu ở bất kỳ vị trí nào trên hàng hiện tại, trả về False
    return False


def print_board(board):
    for row in board:
        print(" ".join(str(col) for col in row))


def main():
    board = [[0 for x in range(8)] for y in range(8)]

    if solve(board, 0):
        print_board(board)
    else:
        print("Không tìm thấy giải pháp")


if __name__ == "__main__":
    main()
