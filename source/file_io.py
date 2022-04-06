import numpy as np

import node


def file_to_node(path: str) -> node.Node:
    file = open(path, "r")
    board = []

    for line in file.readlines():
        # string to int array
        numbers = [int(i) for i in line.split(" ")]

        # skip row with board size
        if len(numbers) < 4:
            continue

        board.append(numbers)

    board = np.array(board)

    file.close()
    return node.Node.get_node(board)


def result_to_file(path: str, solution: [node.Operator]) -> None:
    file = open(path, "w+")
    solution_string = ""

    for operator in solution:
        solution_string += str(operator)

    file.write(str(len(solution)) + '\n')
    file.write(solution_string)
    file.close()


def error_to_file(path: str):
    file = open(path, "w+")
    file.write(str(-1))
    file.close()


def stats_to_file(path: str, solution_length: int,
                  number_of_visited_states: int,
                  number_of_processed_states: int,
                  recursion_depth: int,
                  runtime_duration: float):
    file = open(path, "w+")
    file.write(str(solution_length) + '\n')
    file.write(str(number_of_visited_states) + '\n')
    file.write(str(number_of_processed_states) + '\n')
    file.write(str(recursion_depth) + '\n')
    file.write(str(round(runtime_duration, 3)))
    file.close()
