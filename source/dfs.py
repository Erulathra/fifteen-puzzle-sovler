from collections import deque

from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *


def dfs_algorithm(start_node: Node,
                  search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:
    if start_node.is_goal():
        return start_node
    # crate stack queue and and first node
    stack_queue = deque()
    stack_queue.append(start_node)
    open_set = set()

    while len(stack_queue) != 0:
        # todo: wybadać czemu dodawane są duplikaty
        current_node = stack_queue.popleft()
        if not is_in_stack(current_node, open_set):
            open_set.add(current_node)
            for neighbour in current_node.get_neighbours():
                if neighbour.is_goal():
                    # finish algorithm
                    return neighbour
                if not is_in_stack(neighbour, stack_queue):
                    stack_queue.append(neighbour)

    return None


def is_in_stack(element, stack_queue):
    if element in stack_queue:
        return True
    return False
