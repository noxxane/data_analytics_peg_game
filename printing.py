"""printings funcs"""
from typing import TypeAlias

PADDING = -1
EMPTY = 0
PEG = 1

Board: TypeAlias = list[list[int]]


def print_board(board: Board):
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
                raise ValueError(f"Unrecognized peg value: {peg}")
        print(line_string)


def print_hline():
    """prints a horizontal line, perhaps better described as 'forty hyphens'"""
    print("-" * 40)


def print_initial_board(board: Board):
    """prints an board, preceded by an hline"""
    print_hline()
    print("Initial Board:")
    print_board(board)
    print()
