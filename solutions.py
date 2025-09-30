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
    pos_1_coords = pos_int_to_matrix_coord(pos_1)
    pos_2_coords = pos_int_to_matrix_coord(pos_2)
    # horizontally right
    # horizontally left
    # vertically up
    if (pos_1_coords[0] + 2 == pos_2_coords[0]) and (
        board[pos_1_coords[0] + 1][pos_1_coords[1]] == 1
    ):
        return True
    # vertically down
    if (pos_1_coords[0] - 2 == pos_2_coords[0]) and (
        board[pos_1_coords[0] - 1][pos_1_coords[1]] == 1
    ):
        return True
    # diagonally right-down
    if (
        (pos_1_coords[0] + 2 == pos_2_coords[0])
        and (pos_1_coords[1] + 2 == pos_2_coords[1])
        and (board[pos_1_coords[0] + 1][pos_1_coords[0] + 1] == 1)
    ):
        return True
    # diagonally left-down
    if (
        (pos_1_coords[0] + 2 == pos_2_coords[0])
        and (pos_1_coords[1] - 2 == pos_2_coords[1])
        and (board[pos_1_coords[0] + 1][pos_1_coords[0] - 1] == 1)
    ):
        return True
    # diagonally right-up
    if (
        (pos_1_coords[0] - 2 == pos_2_coords[0])
        and (pos_1_coords[1] + 2 == pos_2_coords[1])
        and (board[pos_1_coords[0] - 1][pos_1_coords[0] + 1] == 1)
    ):
        return True
    # diagonally left-up
    if (
        (pos_1_coords[0] - 2 == pos_2_coords[0])
        and (pos_1_coords[1] - 2 == pos_2_coords[1])
        and (board[pos_1_coords[0] - 1][pos_1_coords[0] - 1] == 1)
    ):
        return True
    else:
        return False


board = [
    [-1, -1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, -1, 1, -1, 1, -1, -1, -1],
    [-1, -1, 1, -1, 1, -1, 1, -1, -1],
    [-1, 1, -1, 1, -1, 1, -1, 1, -1],
    [1, -1, 1, -1, 1, -1, 1, -1, 0],
]

print_board(board)
print(is_move_legal(board, 13, 15))
