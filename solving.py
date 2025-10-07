"""research for data analytics pertaining to the cracker barrel peg game"""

from collections import deque
from typing import TypeAlias
from constants import PADDING, EMPTY, PEG
import constants

Board: TypeAlias = list[list[int]]


def pos_int_to_matrix_coord(pos_int: int) -> tuple[int, int]:
    """translates a position integer to its matrix coordinate"""
    if pos_int in constants.POSITION_MAP:
        return constants.POSITION_MAP[pos_int]
    raise ValueError(f"Invalid position integer: {pos_int}")


def board_element_from_pos_int(board: Board, pos_int: int) -> int:
    """gets a board element from its position integer"""
    row, col = pos_int_to_matrix_coord(pos_int)
    return board[row][col]


def is_move_legal(board: Board, start_pos: int, end_pos: int) -> bool:
    """checks if a move is legal. i could have hardcoded this for each type of
    move (horizontal [1--2 possible], vertical [1--2 possible], diagonal [1--4
    possible]), but this solution takes up fewer lines of code, is simpler and
    easier to understand, and empirically works."""
    legality = False

    start_pos_coords = pos_int_to_matrix_coord(start_pos)
    end_pos_coords = pos_int_to_matrix_coord(end_pos)

    row_diff = end_pos_coords[0] - start_pos_coords[0]
    col_diff = end_pos_coords[1] - start_pos_coords[1]

    # although these numbers might seem strange if you're only looking at the
    # peg game itself, they make sense in the matrix. to jump vertically, you
    # must move -2 or 2 rows; to jump horizontally, you must jump -2 or 2
    # columns. to jump *diagonally*, however, you must jump -2 or 2 rows and -4
    # or 4 columns. hence, this code.
    if (
        row_diff in {-2, 0, 2}
        and col_diff in {-4, -2, 0, 2, 4}
        and (row_diff != 0 or col_diff != 0)
    ):
        legality = True

    middle_row = start_pos_coords[0] + (row_diff // 2)
    middle_col = start_pos_coords[1] + (col_diff // 2)
    middle_occupied = board[middle_row][middle_col] == PEG

    beginning_occupied = board_element_from_pos_int(board, start_pos) == PEG
    end_unoccupied = board_element_from_pos_int(board, end_pos) == EMPTY
    legality = legality and beginning_occupied and middle_occupied and end_unoccupied

    return legality


def make_move(board: Board, start_pos: int, end_pos: int) -> Board:
    """makes a move by creating a copy of the given board, making the move (and
    checking the move's legality), and returning the new board with the move
    made."""
    if not is_move_legal(board, start_pos, end_pos):
        raise ValueError(
            f"Illegal move: cannot move from position {start_pos} to {end_pos}"
        )

    new_board = [row[:] for row in board]
    start_pos_coords = pos_int_to_matrix_coord(start_pos)
    end_pos_coords = pos_int_to_matrix_coord(end_pos)

    row_diff = end_pos_coords[0] - start_pos_coords[0]
    col_diff = end_pos_coords[1] - start_pos_coords[1]

    middle_row = start_pos_coords[0] + (row_diff // 2)
    middle_col = start_pos_coords[1] + (col_diff // 2)

    new_board[start_pos_coords[0]][start_pos_coords[1]] = 0
    new_board[middle_row][middle_col] = 0
    new_board[end_pos_coords[0]][end_pos_coords[1]] = 1

    return new_board


def possible_moves(board: Board) -> list[tuple[int, int]]:
    """checks every possible legal (doesn't check for midpoint, but does check
    for peg in start position and an empty hole in the end position) position
    for every possible move. then ensures it's legal and returns the list of
    moves."""
    moves = []

    possible_start_pos = [
        x
        for x in range(constants.MIN_POSITION, constants.MAX_POSITION + 1)
        if board_element_from_pos_int(board, x) == PEG
    ]
    possible_end_pos = [
        x
        for x in range(constants.MIN_POSITION, constants.MAX_POSITION + 1)
        if board_element_from_pos_int(board, x) == EMPTY
    ]
    for start_pos in possible_start_pos:
        for end_pos in possible_end_pos:
            if is_move_legal(board, start_pos, end_pos):
                moves.append((start_pos, end_pos))

    return moves


def is_board_solved(board: Board) -> bool:
    """checks if a board is solved by counting the pegs left on the board"""
    return sum(cell == PEG for row in board for cell in row) == 1


def board_to_tuple(board: Board) -> tuple:
    """converts a board to a tuple so it's easier to solve"""
    return tuple(tuple(row) for row in board)


def brute_force_board(board: Board) -> list[tuple[int, int]] | None:
    """uses a brute force method to solve a board. for every possible move,
    make that move and see if the board's solved. if it's solved, then return
    the move list."""
    queue = deque([(board, [])])
    visited = set()
    visited.add(board_to_tuple(board))

    while queue:
        current_board, path = queue.popleft()

        if is_board_solved(current_board):
            return path

        moves = possible_moves(current_board)

        for move in moves:
            new_board = make_move(current_board, move[0], move[1])
            board_state = board_to_tuple(new_board)

            if board_state not in visited:
                visited.add(board_state)
                queue.append((new_board, path + [move]))

    return None


def brute_force_all_solutions(board: Board) -> list[list[tuple[int, int]]]:
    """uses a brute force method to find all possible solutions from a given
    starting board"""
    queue = deque([(board, [])])
    visited_with_path = {}
    all_solutions = []

    initial_state = board_to_tuple(board)
    visited_with_path[initial_state] = {tuple()}

    while queue:
        current_board, path = queue.popleft()

        if is_board_solved(current_board):
            all_solutions.append(path)
            continue

        moves = possible_moves(current_board)

        for move in moves:
            new_board = make_move(current_board, move[0], move[1])
            board_state = board_to_tuple(new_board)
            new_path = path + [move]
            path_tuple = tuple(new_path)

            if board_state not in visited_with_path:
                visited_with_path[board_state] = {path_tuple}
                queue.append((new_board, new_path))
            elif path_tuple not in visited_with_path[board_state]:
                visited_with_path[board_state].add(path_tuple)
                queue.append((new_board, new_path))

    return all_solutions


def solve_board(
    board: Board, path: list[tuple[int, int]], visited: set[tuple]
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


def create_full_board() -> Board:
    """creates a full board, with every peg hole filled"""
    board = [
        [PADDING, PADDING, PADDING, PADDING, PEG, PADDING, PADDING, PADDING, PADDING],
        [PADDING, PADDING, PADDING, PEG, PADDING, PEG, PADDING, PADDING, PADDING],
        [PADDING, PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING, PADDING],
        [PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING],
        [PEG, PADDING, PEG, PADDING, PEG, PADDING, PEG, PADDING, PEG],
    ]

    return board
