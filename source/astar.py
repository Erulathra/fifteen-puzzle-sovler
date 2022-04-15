from node import *
import heapq_decorator as hd


def a_star(heuristic: str, start_node_path: str, solution_path: str, statistics_path: str):
    pass


def a_star_algorithm(start_node: Node, heuristic) -> Node:
    if start_node.is_goal():
        return start_node
    # crate priority queue and and first node
    priority_queue = hd.HeapqDecorator()
    open_set = set()

    while len(priority_queue) != 0:
        current_node: Node = priority_queue.pop()
        if current_node.is_goal():
            return current_node

        open_set.add(current_node)

        for neighbour in current_node.get_neighbours():
            if not (neighbour in open_set):
                neighbour_priority = priority_queue.priority(current_node) + heuristic(neighbour)
                if not priority_queue.contains(neighbour):
                    priority_queue.push(neighbour_priority, neighbour)
                elif priority_queue.priority(neighbour) > neighbour_priority:
                    priority_queue.update(neighbour_priority, neighbour)

    return None


def hamming_heuristic(node: Node) -> int:
    valid_board = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    return np.count_nonzero(node.board == valid_board)
