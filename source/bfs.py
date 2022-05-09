from collections import deque

from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *


def bfs_algorithm(start_node: Node,
                  order: str = "LURD",
                  search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:
    # prepare statistics object
    search_statistics.start_runtime_measure()
    
    if start_node.is_goal():
        return start_node
    # crate stack queue and and first node
    open_deque = deque()
    open_deque.append(start_node)
    search_statistics.increase_visited_states_count(1)
    closed_set = set()
    closed_set.add(start_node)
    search_statistics.increase_processed_states_count(1)

    while len(open_deque):
        current_node = open_deque.popleft()
        for neighbour in current_node.get_neighbours(order):
            search_statistics.change_max_recursion_depth(neighbour.depth)
            if neighbour.is_goal():
                # finish algorithm
                search_statistics.stop_runtime_measure()
                search_statistics.calculate_solution_length(neighbour.path)
                return neighbour
            # check if neighbour is in closed_set based on field values
            if neighbour not in closed_set:
                closed_set.add(neighbour)
                search_statistics.increase_processed_states_count(1)
                open_deque.append(neighbour)
                search_statistics.increase_visited_states_count(1)

    search_statistics.stop_runtime_measure()
    return None
