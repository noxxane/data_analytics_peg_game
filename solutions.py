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
    elif 2 <= pos_int <= 3:
        r = 1
        c = (2 * pos_int) - 1
        return (r, c)
    elif 4 <= pos_int <= 6:
        r = 2
        c = (2 * pos_int) - 6
        return (r, c)
    elif 7 <= pos_int <= 10:
        r = 3
        c = (2 * pos_int) - 13
        return (r, c)
    elif 11 <= pos_int <= 15:
        r = 4
        c = (pos_int - 11) * 2
        return (r, c)
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
