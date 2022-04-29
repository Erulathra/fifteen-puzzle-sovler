import numpy as np

import node
from ISearchStatistics import ISearchStatistics


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


def result_to_file(path: str, solution_node: node.Node) -> None:
    with open(path, "w+") as file:
        file.write(str(len(solution_node.path)) + '\n')
        file.write(solution_node.path)


def error_to_file(path: str):
    with open(path, "w+") as file:
        file.write(str(-1))


def stats_to_file(path: str, search_statistics: ISearchStatistics):
    with open(path, "w+") as file:
        file.write(str(search_statistics.solution_length) + '\n')
        file.write(str(search_statistics.visited_states_count) + '\n')
        file.write(str(search_statistics.processed_states_count) + '\n')
        file.write(str(search_statistics.max_recursion_depth) + '\n')
        file.write(str(round(search_statistics.run_time, 3)))
