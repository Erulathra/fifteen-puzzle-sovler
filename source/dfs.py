from collections import deque

from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *


def dfs_algorithm(start_node: Node,
                  search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:
    if start_node.is_goal():
        return start_node
    # crate stack queue and and first node
    stack = deque()
    stack.append(start_node)
    closed_set = set()

    while len(stack):
        current_node = stack.popleft()
        if current_node not in closed_set:
            closed_set.add(current_node)
            for neighbour in current_node.get_neighbours():
                if neighbour.is_goal():
                    # finish algorithm
                    return neighbour
                stack.append(neighbour)

    return None
