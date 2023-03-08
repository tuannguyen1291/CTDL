def is_valid_move(board, row, col, N):
    """
    Kiểm tra nước đi có hợp lệ hay không
    """
    # Kiểm tra cột
    for i in range(N):
        if board[row][i] == 1:
            return False

    # Kiểm tra đường chéo chính
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j - 1

    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j + 1

    return True


def print_solution(board):
    """
    In ra ma trận giải pháp
    """
    for row in board:
        print(row)


def solve_n_queens(board, row, N):
    """
    Tìm giải pháp cho bài toán 8 con xe bằng backtracking
    """
    # Nếu đã đặt được 8 con xe thì in ra giải pháp
    if row == N:
        print_solution(board)
        return True

    # Duyệt qua các cột để đặt con xe vào
    for col in range(N):
        if is_valid_move(board, row, col, N):
            # Đặt con xe vào vị trí (row, col)
            board[row][col] = 1

            # Gọi đệ quy để đặt các con xe tiếp theo
            if solve_n_queens(board, row + 1, N):
                return True

            # Nếu không tìm được giải pháp, bỏ con xe khỏi vị trí (row, col)
            board[row][col] = 0

    # Nếu không thể đặt con xe vào bất kỳ vị trí nào trong cột hiện tại, trả về False
    return False
