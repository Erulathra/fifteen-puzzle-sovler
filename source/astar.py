from queue import PriorityQueue
from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *


def a_star(heuristic: str, start_node_path: str, solution_path: str, statistics_path: str):
    pass


def a_star_algorithm(start_node: Node,
                     heuristic,
                     search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:
    search_statistics.start_runtime_measure()

    if start_node.is_goal():
        return start_node
    # crate priority queue and and first node
    open_priority_queue = PriorityQueue()
    open_priority_queue.put((0, 0, start_node))
    search_statistics.increase_visited_states_count(1)

    closed_set = set()

    visited_id = 0

    while not open_priority_queue.empty():
        current_priority, node_id, current_node = open_priority_queue.get()

        if current_node in closed_set:
            continue

        search_statistics.change_max_recursion_depth(current_node.depth)
        if current_node.is_goal():
            # finish algorithm
            search_statistics.stop_runtime_measure()
            search_statistics.calculate_solution_length(current_node.path)
            return current_node

        closed_set.add(current_node)
        search_statistics.increase_processed_states_count(1)

        for neighbour in current_node.get_neighbours():
            if neighbour in closed_set:
                continue

            neighbour_priority = current_priority + heuristic(neighbour)
            open_priority_queue.put((neighbour_priority, visited_id, neighbour))
            search_statistics.increase_visited_states_count(1)
            visited_id += 1

    search_statistics.stop_runtime_measure()
    return None


def hamming_heuristic(node: Node) -> int:
    return 16 - np.count_nonzero(node.board == node.target_board)


def manhattan_heuristic(node: Node) -> int:
    result = 0
    board = node.board
    target_board = node.target_board

    for i in range(target_board.shape[0]):
        for j in range(target_board.shape[1]):
            position = np.where(board == target_board[i][j])
            result += np.absolute(position[0][0] - i) + np.absolute(position[1][0] - j)

    return result
