from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import Node


def dfs_algorithm(start_node: Node,
                  order: str = "LURD",
                  search_statistics: ISearchStatistics = NoneSearchStatistics(),
                  max_depth: int = 25):
    search_statistics.start_runtime_measure()

    if start_node.is_goal():
        search_statistics.stop_runtime_measure()
        search_statistics.calculate_solution_length(start_node.path)
        return start_node

    open_stack = [start_node]
    closed_set = set()

    search_statistics.increase_visited_states_count(1)

    while open_stack:
        current_node = open_stack.pop()

        if current_node in closed_set or current_node.depth > max_depth:
            continue

        closed_set.add(current_node)
        search_statistics.increase_processed_states_count(1)

        for neighbour in reversed(current_node.get_neighbours(order)):
            search_statistics.change_max_recursion_depth(neighbour.depth)

            if neighbour.is_goal():
                search_statistics.stop_runtime_measure()
                search_statistics.calculate_solution_length(neighbour.path)
                return neighbour

            open_stack.append(neighbour)
            search_statistics.increase_visited_states_count(1)

    search_statistics.stop_runtime_measure()
    return None
