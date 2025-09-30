def print_board(board: list[list]):
    for line in board:
        line_string = ""
        for peg in line:
            if peg == -1:
                line_string += " "
            elif peg == 0:
                line_string += "O"
            elif peg == 1:
                line_string += "I"
            else:
                print("Don't recognize peg value. Skibidi!")
        print(line_string)


def pos_int_to_matrix_coord(pos_int) -> tuple[int, int]:
    if pos_int == 1:
        return (0, 4)
    elif pos_int == 2:
        return (1, 3)
    elif pos_int == 3:
        return (1, 5)
    elif pos_int == 4:
        return (2, 2)
    elif pos_int == 5:
        return (2, 4)
    elif pos_int == 6:
        return (2, 6)
    elif pos_int == 7:
        return (3, 1)
    elif pos_int == 8:
        return (3, 3)
    elif pos_int == 9:
        return (3, 5)
    elif pos_int == 10:
        return (3, 7)
    elif pos_int == 11:
        return (4, 0)
    elif pos_int == 12:
        return (4, 2)
    elif pos_int == 13:
        return (4, 4)
    elif pos_int == 14:
        return (4, 6)
    elif pos_int == 15:
        return (4, 8)
    else:
        print("Don't recognize pos_int. Skibidi!")
        # out of range index values
        return (6, 10)


def is_move_legal(board: list[list], pos_1: int, pos_2: int) -> bool:
    legality = False

    pos_1_coords = pos_int_to_matrix_coord(pos_1)
    pos_2_coords = pos_int_to_matrix_coord(pos_2)

    row_diff = pos_2_coords[0] - pos_1_coords[0]
    col_diff = pos_2_coords[1] - pos_1_coords[1]

    if (row_diff in {-4, 0, 4} and col_diff in {-4, 0, 4}) and (
        row_diff != 0 or col_diff != 0
    ):
        legality = True

    middle_row = pos_1_coords[0] + (row_diff // 2)
    middle_col = pos_1_coords[1] + (col_diff // 2)
    middle_occupied = True if board[middle_row][middle_col] == 1 else False

    beginning_occupied = board[pos_1_coords[0]][pos_1_coords[1]] == 1
    end_unoccupied = board[pos_2_coords[0]][pos_2_coords[1]] == 0
    legality = legality and beginning_occupied and middle_occupied and end_unoccupied

    return legality


def make_move(board: list[list], pos_1: int, pos_2: int) -> list[list]:
    new_board = board
    if is_move_legal(board, pos_1, pos_2):
        pos_1_coords = pos_int_to_matrix_coord(pos_1)
        pos_2_coords = pos_int_to_matrix_coord(pos_2)

        row_diff = pos_2_coords[0] - pos_1_coords[0]
        col_diff = pos_2_coords[1] - pos_1_coords[1]

        middle_row = pos_1_coords[0] + (row_diff // 2)
        middle_col = pos_1_coords[1] + (col_diff // 2)

        new_board[pos_1_coords[0]][pos_1_coords[1]] = 0
        new_board[middle_row][middle_col] = 0
        new_board[pos_2_coords[0]][pos_2_coords[1]] = 1
    return new_board


board = [
    [-1, -1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, -1, 1, -1, 1, -1, -1, -1],
    [-1, -1, 1, -1, 1, -1, 1, -1, -1],
    [-1, 1, -1, 1, -1, 1, -1, 1, -1],
    [1, -1, 1, -1, 1, -1, 1, -1, 0],
]

print_board(board)
board = make_move(board, 13, 15)
print_board(board)
