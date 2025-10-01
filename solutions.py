"""research for data analytics pertaining to the cracker barrel peg game"""

import copy

PADDING = -1
EMPTY = 0
PEG = 1

BOARD_HEIGHT = 5
BOARD_WIDTH = 9
NUM_POSITIONS = 15

MIN_POSITION = 1
MAX_POSITION = 15


def print_board(board: list[list]):
    """prints a board in a readable format where padding spaces are not
    printed, empty spaces are printed as O, and spaces with pegs are printed as
    I"""
    for line in board:
        line_string = ""
        for peg in line:
            if peg == PADDING:
                line_string += " "
            elif peg == EMPTY:
                line_string += "O"
            elif peg == PEG:
                line_string += "I"
            else:
                print("Don't recognize peg value.")
        print(line_string)


def pos_int_to_matrix_coord(pos_int) -> tuple[int, int]:
    """translates a position integer to its matrix coordinate; 1, for instance,
    has the matrix coordinate (0, 4). this is a relatively hacky solution,
    where i found linear functions which translate the positions rather than
    hardcoding them. but it uses significantly fewer lines of code, and that's
    my metric of success"""
    if pos_int == 1:
        return (0, 4)
    if 2 <= pos_int <= 3:
        r = 1
        c = (2 * pos_int) - 1
        return (r, c)
    if 4 <= pos_int <= 6:
        r = 2
        c = (2 * pos_int) - 6
        return (r, c)
    if 7 <= pos_int <= 10:
        r = 3
        c = (2 * pos_int) - 13
        return (r, c)
    if 11 <= pos_int <= 15:
        r = 4
        c = (pos_int - 11) * 2
        return (r, c)
    print("Don't recognize pos_int.")
    # out of range index values
    return (6, 10)


def is_move_legal(board: list[list], pos_1: int, pos_2: int) -> bool:
    """checks if a move is legal. i could have hardcoded this for each type of
    move (horizontal [1--2 possible], vertical [1--2 possible], diagonal [1--4
    possible]), but this solution takes up fewer lines of code, is simpler and
    easier to understand, and empirically works."""
    legality = False

    pos_1_coords = pos_int_to_matrix_coord(pos_1)
    pos_2_coords = pos_int_to_matrix_coord(pos_2)

    row_diff = pos_2_coords[0] - pos_1_coords[0]
    col_diff = pos_2_coords[1] - pos_1_coords[1]

    if (row_diff in {-2, 0, 2} and col_diff in {-4, -2, 0, 2, 4}) and (
        row_diff != 0 or col_diff != 0
    ):
        legality = True

    middle_row = pos_1_coords[0] + (row_diff // 2)
    middle_col = pos_1_coords[1] + (col_diff // 2)
    middle_occupied = board[middle_row][middle_col] == 1

    beginning_occupied = board[pos_1_coords[0]][pos_1_coords[1]] == 1
    end_unoccupied = board[pos_2_coords[0]][pos_2_coords[1]] == 0
    legality = legality and beginning_occupied and middle_occupied and end_unoccupied

    return legality


def make_move(board: list[list], pos_1: int, pos_2: int) -> list[list]:
    """makes a move by creating a copy of the given board, making the move (and
    checking the move's legality), and returning the new board with the move
    made."""
    new_board = copy.deepcopy(board)
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


def possible_moves(board: list[list]) -> list[tuple[int, int]]:
    """checks every possible position for every possible move by checking the
    legality on the given board. there is likely a more efficient way to do
    this, but the solution space is so low that the program runs very quickly
    anyway. (checking if pos_2 is occupied, for instance, would eliminate up to
             14 possible moves)"""
    possible_moves_list = []
    for pos_1 in range(MIN_POSITION, MAX_POSITION + 1):
        for pos_2 in range(MIN_POSITION, MAX_POSITION + 1):
            if is_move_legal(board, pos_1, pos_2):
                possible_moves_list.append((pos_1, pos_2))

    return possible_moves_list


def is_board_solved(board: list[list]) -> bool:
    """checks if a board is solved by counting the pegs left on the board"""
    pegs_remaining = 0
    for row in board:
        pegs_remaining += row.count(PEG)
    if pegs_remaining == 1:
        return True
    return False


def board_to_tuple(board: list[list]) -> tuple:
    """converts a board to a tuple so it's easier to solve"""
    return tuple(tuple(row) for row in board)


def solve_board(
    board: list[list], path: list[tuple[int, int]], visited: set
) -> list[tuple[int, int]] | None:
    """recursively solves a board using a dfs, or depth first search. it goes
    down each possible move path, backtracking if the path ends without finding
    a solution."""
    board_state = board_to_tuple(board)
    if board_state in visited:
        return None
    visited.add(board_state)

    if is_board_solved(board):
        return path

    moves = possible_moves(board)

    if not moves:
        return None

    for move in moves:
        new_board = make_move(board, move[0], move[1])
        result = solve_board(new_board, path + [move], visited)

        if result is not None:
            return result

    return None

def create_full_board() -> list[list]:
    """crestes a full board, with every peg hole filled"""
    board = [
        [PADDING, PADDING, PADDING, PADDING, PEG, PADDING, PADDING, PADDING, PADDING],
        [PADDING, PADDING, PADDING, PEG, PADDING, PEG, PADDING, PADDING, PADDING],
        [PADDING, PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING, PADDING],
        [PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING],
        [PEG, PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING, PEG],
    ]

    return board

def main():
    """main func"""
    for position in range(MIN_POSITION, MAX_POSITION + 1):
        board = create_full_board()

        matrix_coord_of_pos_int = pos_int_to_matrix_coord(position)
        row = matrix_coord_of_pos_int[0]
        col = matrix_coord_of_pos_int[1]
        board[row][col] = EMPTY

        print("Initial board:")
        print_board(board)
        print()

        print(f"Solving with starting empty position: {position}")
        visited_states = set()
        solution = solve_board(board, [], visited_states)

        if solution:
            print(f"Found solution with {len(solution)} steps.")
            print()
            print("Move sequence:")
            for step_num, move in enumerate(solution, 1):
                print(f"{step_num}. Move from position {move[0]} to {move[1]}.")

            print()
            print("Final board:")
            final_board = copy.deepcopy(board)
            for move in solution:
                final_board = make_move(final_board, move[0], move[1])
            print_board(final_board)
        else:
            print("No solution found.")


if __name__ == "__main__":
    main()
