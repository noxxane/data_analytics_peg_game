"""main file for peg game solving"""

import argparse
import copy
import time
import constants
import printing
import solving


def main_dfs():
    """main dfs func"""
    start_time = time.perf_counter()

    for position in range(constants.MIN_POSITION, constants.MAX_POSITION + 1):
        board = solving.create_full_board()

        row, col = solving.pos_int_to_matrix_coord(position)
        board[row][col] = constants.EMPTY

        printing.print_initial_board(board)

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

            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.6f} seconds")

            printing.print_board(final_board)
        else:
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.6f} seconds")

            print("No solution found.")


def main_brute(position: int):
    """main brute func"""
    start_time = time.perf_counter()

    board = solving.create_full_board()

    row, col = solving.pos_int_to_matrix_coord(position)
    board[row][col] = constants.EMPTY

    printing.print_initial_board(board)

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
        printing.print_board(final_board)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
    else:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")

        print("No solution found.")


def main_brute_all_solutions(position: int):
    """main brute all solutions func"""
    start_time = time.perf_counter()

    board = solving.create_full_board()

    row, col = solving.pos_int_to_matrix_coord(position)
    board[row][col] = constants.EMPTY

    printing.print_initial_board(board)

    print(f"Solving with starting empty position: {position}")
    solutions = solving.brute_force_all_solutions(board)

    if solutions:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")

        print(f"Found {len(solutions)} total solutions.")
        print()

        for sol_num, solution in enumerate(solutions, 1):
            print(f"Solution #{sol_num} ({len(solution)} moves):")
            for step_num, move in enumerate(solution, 1):
                print(f"    {step_num}. Move from position {move[0]} to {move[1]}.")
            print()
    else:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")

        print("No solution found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="peg_board_solver", description="solves peg game"
    )

    parser.add_argument("solver")
    parser.add_argument("position")

    args = parser.parse_args()
    # if args.solver == "dfs":
    #     main_dfs(args.position)
    user_position = int(args.position)
    if args.solver == "brute":
        main_brute(user_position)
    elif args.solver == "brute_all_solutions":
        main_brute_all_solutions(user_position)
    else:
        print("don't recognize solver. options are: 'brute', 'brute_all_solutions'")
