from collections import deque

from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *


def dfs_algorithm(start_node: Node,
                  order: str = "LURD",
                  search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:
    search_statistics.start_runtime_measure()

    if start_node.is_goal():
        return start_node
    # crate stack queue and and first node
    stack: deque[Node] = deque()
    stack.append(start_node)
    search_statistics.increase_visited_states_count(1)
    closed_set: set[Node] = set()

    while len(stack):
        current_node = stack.popleft()
        if len(current_node.path) > 20:
            continue

        if current_node not in closed_set:
            closed_set.add(current_node)
            search_statistics.increase_processed_states_count(1)
            for neighbour in current_node.get_neighbours(order):
                search_statistics.change_max_recursion_depth(len(neighbour.path))
                if neighbour.is_goal():
                    # finish algorithm
                    search_statistics.stop_runtime_measure()
                    search_statistics.calculate_solution_length(neighbour.path)
                    return neighbour
                stack.append(neighbour)
                search_statistics.increase_visited_states_count(1)

    return None
