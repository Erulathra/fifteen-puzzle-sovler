from collections import deque

from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import Node


def dfs_algorithm(start_node: Node,
                  order: str = "LURD",
                  search_statistics: ISearchStatistics = NoneSearchStatistics()):
    search_statistics.start_runtime_measure()

    if start_node.is_goal():
        return start_node
    # crate stack queue and and first node
    open_stack: list[Node] = [start_node]
    closed_set: set[Node] = set()

    search_statistics.increase_visited_states_count(1)

    while open_stack:
        current_node = open_stack.pop()

        if current_node in closed_set or current_node.depth > 25:
            continue

        closed_set.add(current_node)
        search_statistics.increase_processed_states_count(1)

        for neighbour in reversed(current_node.get_neighbours(order)):
            if current_node.is_goal():
                # finish algorithm
                search_statistics.stop_runtime_measure()
                search_statistics.calculate_solution_length(current_node.path)
                return current_node

            open_stack.append(neighbour)
            search_statistics.increase_visited_states_count(1)
            search_statistics.change_max_recursion_depth(neighbour.depth)

    search_statistics.stop_runtime_measure()
    return None

