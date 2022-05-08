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
        search_statistics.change_max_recursion_depth(current_node.depth)

        if current_node.is_goal():
            # finish algorithm
            search_statistics.stop_runtime_measure()
            search_statistics.calculate_solution_length(current_node.path)
            return current_node

        if current_node in closed_set:
            if not update_closed_set(current_node, closed_set):
                continue

        if current_node.depth > 20:
            continue

        closed_set.add(current_node)
        search_statistics.increase_processed_states_count(1)

        for neighbour in reversed(current_node.get_neighbours(order)):
            open_stack.append(neighbour)
            search_statistics.increase_visited_states_count(1)

    return None


def update_closed_set(node, nodes_set):
    try:
        nodes_set.remove(node)
        return True
    except Exception:
        return False
