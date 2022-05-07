from unittest import TestCase

import numpy as np

import dfs
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

    test_board_2 = np.array([
        [1, 0, 3, 4],
        [5, 2, 7, 8],
        [10, 6, 11, 12],
        [9, 13, 14, 15]
    ])
    test_nodes.append(Node.get_node(test_board_2))

    def test_dfs_algorithm(self):
        for test_node in [self.test_nodes[1]]:
            try:
                result = dfs.dfs_algorithm(test_node)
            except:
                self.fail("Couldn't find solution")
            else:
                self.assertTrue(result.is_goal())
