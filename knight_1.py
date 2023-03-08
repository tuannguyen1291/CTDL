def is_valid_move(x, y, board, n):
    """
    Kiểm tra nước đi có hợp lệ hay không
    """
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False

def knights_tour(n):
    """
    Tìm đường đi của quân mã trên bàn cờ nxn
    """
    # Tạo bàn cờ trống
    board = [[-1 for i in range(n)] for j in range(n)]

    # Các bước di chuyển của quân mã
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    # Đặt quân mã tại ô đầu tiên
    board[0][0] = 0

    # Sử dụng đệ quy để tìm đường đi
    if not knights_tour_helper(0, 0, 1, board, n, x_move, y_move):
        print("Không tìm được đường đi cho quân mã")
    else:
        print_board(board, n)

def knights_tour_helper(x, y, move_no, board, n, x_move, y_move):
    """
    Hàm đệ quy để tìm đường đi của quân mã
    """
    # Nếu tất cả các ô trên bàn cờ đã được thăm
    if move_no == n * n:
        return True

    # Thử tất cả các nước đi có thể
    for i in range(8):
        next_x = x + x_move[i]
        next_y = y + y_move[i]
        if is_valid_move(next_x, next_y, board, n):
            board[next_x][next_y] = move_no
            if knights_tour_helper(next_x, next_y, move_no + 1, board, n, x_move, y_move):
                return True
            board[next_x][next_y] = -1

    return False

def print_board(board, n):
    """
    In bàn cờ
    """
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

# Thử nghiệm
n = int(input("Nhap vao n: "))
knights_tour(n)
