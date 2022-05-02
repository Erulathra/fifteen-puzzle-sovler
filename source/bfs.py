from collections import deque
from inspect import stack
from ISearchStatistics import ISearchStatistics, NoneSearchStatistics
from node import *

def bfs_algorithm(start_node: Node,
					search_statistics: ISearchStatistics = NoneSearchStatistics()) -> Node:
	
	if start_node.is_goal():
		return start_node
	# crate stack queue and and first node
	stack_queue = deque()
	stack_queue.append(start_node)
	open_set = set()
	open_set.add(start_node)

	while len(stack_queue) != 0:
		current_node = stack_queue.popleft()
		for neighbour in current_node.get_neighbours():
			if neighbour.is_goal():
				# finish algorithm
				return neighbour
			# check if neighbour is in open_set based on field values
			if not is_in_stack(neighbour, open_set):
				open_set.add(neighbour)
				stack_queue.append(neighbour)

	return None


def is_in_stack(element, stack_queue):
	for stack_element in stack_queue:
		if (element.board == stack_element.board).all() and \
			(element.zero_position == stack_element.zero_position).all():
			return True
	return False