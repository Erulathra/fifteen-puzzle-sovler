from unittest import TestCase

import numpy as np

import astar
from node import Node


class Heuristics_Test(TestCase):
    test_board_1 = np.array([   # Manhattan             # Hamming
        [5, 6, 7, 8],           # 1 + 1 + 1 + 1 = 4     # 1 + 1 + 1 + 1 = 4
        [4, 3, 2, 1],           # 4 + 2 + 2 + 4 = 12    # 1 + 1 + 1 + 1 = 4
        [12, 11, 10, 9],        # 3 + 1 + 1 + 3 = 8     # 1 + 1 + 1 + 1 = 4
        [13, 14, 15, 0]         # 0 + 0 + 0 + 0 = 0     # 0 + 0 + 0 + 0 = 0
    ])                          # ------------ += 24    # ------------ += 12
    test_node_1 = Node.get_node(test_board_1)

    def test_hamming_heuristic(self):
        self.assertEqual(12, astar.hamming_heuristic(self.test_node_1))

    def test_manhattan_heuristic(self):
        self.assertEqual(24, astar.manhattan_heuristic(self.test_node_1))
