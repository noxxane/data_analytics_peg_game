"""main file for peg game solving"""
import copy
import solving

PADDING = -1
EMPTY = 0
PEG = 1

MIN_POSITION = 1
MAX_POSITION = 15


def main_dfs():
    """main dfs func"""
    for position in range(MIN_POSITION, MAX_POSITION + 1):
        board = solving.create_full_board()

        row, col = solving.pos_int_to_matrix_coord(position)
        board[row][col] = EMPTY

        solving.print_initial_board(board)

        print(f"Solving with starting empty position: {position}")
        visited_states = set()
        solution = solving.solve_board(board, [], visited_states)

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
                final_board = solving.make_move(final_board, move[0], move[1])
            solving.print_board(final_board)
        else:
            print("No solution found.")


def main_brute():
    """main brute func"""
    position = 1
    board = solving.create_full_board()

    row, col = solving.pos_int_to_matrix_coord(position)
    board[row][col] = EMPTY

    solving.print_initial_board(board)

    print(f"Solving with starting empty position: {position}")
    solution = solving.brute_force_board(board)

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
            final_board = solving.make_move(final_board, move[0], move[1])
        solving.print_board(final_board)
    else:
        print("No solution found.")


def main_brute_all_solutions():
    """main brute all solutions func"""
    position = 1
    board = solving.create_full_board()

    row, col = solving.pos_int_to_matrix_coord(position)
    board[row][col] = EMPTY

    solving.print_initial_board(board)

    print(f"Solving with starting empty position: {position}")
    solutions = solving.brute_force_all_solutions(board)

    if solutions:
        print(f"Found {len(solutions)} total solutions.")
        print()

        for sol_num, solution in enumerate(solutions, 1):
            print(f"Solution #{sol_num} ({len(solution)} moves):")
            for step_num, move in enumerate(solution, 1):
                print(f"    {step_num}. Move from position {move[0]} to {move[1]}.")
            print()
    else:
        print("No solution found.")


if __name__ == "__main__":
    main_brute_all_solutions()
