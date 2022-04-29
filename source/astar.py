import heapq_decorator as hd
from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *


def a_star(heuristic: str, start_node_path: str, solution_path: str, statistics_path: str):
    pass


def a_star_algorithm(start_node: Node,
                     heuristic,
                     search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:

    # prepare statistics object
    search_statistics.increase_processed_states_count(1)
    search_statistics.increase_visited_states_count(1)
    search_statistics.start_runtime_measure()

    if start_node.is_goal():
        return start_node
    # crate priority queue and and first node
    priority_queue = hd.HeapqDecorator()
    priority_queue.push(0, start_node)
    open_set = set()

    while len(priority_queue) != 0:
        current_priority, current_node = priority_queue.pop()
        search_statistics.increase_processed_states_count(1)
        search_statistics.change_max_recursion_depth(len(current_node.path))
        if current_node.is_goal():
            # finish algorithm
            search_statistics.end_runtime_measure()
            search_statistics.calculate_solution_length(current_node.path)
            return current_node

        open_set.add(current_node)
        for neighbour in current_node.get_neighbours():
            if not (neighbour in open_set):
                neighbour_priority = current_priority + heuristic(neighbour)
                search_statistics.increase_visited_states_count(1)
                if not priority_queue.contains(neighbour):
                    priority_queue.push(neighbour_priority, neighbour)
                elif priority_queue.priority(neighbour) > neighbour_priority:
                    priority_queue.update(neighbour_priority, neighbour)

    return None


def hamming_heuristic(node: Node) -> int:
    valid_board = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    return 16 - np.count_nonzero(node.board == valid_board)


def manhattan_heuristic(node: Node) -> int:
    result = 0
    board = node.board

    for i in range(4):
        for j in range(4):
            # this complicated formula increases demanded number form 1 to 15, but the last number is 0
            position = np.where(board == (i * 4 + j + 1) % 16)
            result += np.absolute(position[0][0] - i) + np.absolute(position[1][0] - j)

    return result
