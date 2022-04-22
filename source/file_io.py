import numpy as np

import node


def file_to_node(path: str) -> node.Node:
    board = []

    with open(path, "r") as file:
        lines = file.readlines()

        board_width, board_height = lines[0].split(" ")

    for line in lines[1:]:
        # string to int array
        numbers = [int(i) for i in line.split(" ")]

        board.append(numbers)

    board = np.array(board)

    file.close()
    return node.Node.get_node(board)


def result_to_file(path: str, solution: [node.Operator]) -> None:
    with open(path, "w+") as file:
        solution_string = ""

        for operator in solution:
            solution_string += str(operator)

        file.write(str(len(solution)) + '\n')
        file.write(solution_string)


def error_to_file(path: str):
    with open(path, "w+") as file:
        file.write(str(-1))


def stats_to_file(path: str, solution_length: int,
                  number_of_visited_states: int,
                  number_of_processed_states: int,
                  recursion_depth: int,
                  runtime_duration: float):
    with open(path, "w+") as file:
        file.write(str(solution_length) + '\n')
        file.write(str(number_of_visited_states) + '\n')
        file.write(str(number_of_processed_states) + '\n')
        file.write(str(recursion_depth) + '\n')
        file.write(str(round(runtime_duration, 3)))
