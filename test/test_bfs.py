from unittest import TestCase

import numpy as np

import bfs
from node import Node

class algorithm_test(TestCase):
	test_nodes = []
	test_board_0 = np.array([
		[1, 2, 3, 4],
		[5, 6, 0, 8],
		[9, 11, 7, 12],
		[13, 10, 14, 15]
	])
	test_nodes.append(Node.get_node(test_board_0))

	test_board_1 = np.array([
		[0, 1, 9, 8],
		[10, 7, 14, 15],
		[5, 12, 3, 13],
		[4, 11, 6, 2]
	])
	test_nodes.append(Node.get_node(test_board_1))

	test_board_2 = np.array([
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 0, 14, 15]
	])
	test_nodes.append(Node.get_node(test_board_2))

	def test_bfs_algorithm(self):
		for test_node in self.test_nodes:
			try:
				result = bfs.bfs_algorithm(test_node)
			except:
				self.fail("Couldn't find solution")
			else:
				self.assertTrue(result.is_goal())
