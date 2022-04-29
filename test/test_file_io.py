import time
from unittest import TestCase

import numpy as np

import file_io
import node
from SearchStatistics import SearchStatistics


class Test(TestCase):
    board = np.array([[1, 6, 2, 3],
                      [5, 7, 0, 4],
                      [9, 10, 11, 8],
                      [13, 14, 15, 12]])
    zero_position = np.array([2, 1])

    board_3x3 = np.array([[1, 2, 3],
                          [4, 6, 0],
                          [7, 5, 8]])
    zero_position_3x3 = np.array([2, 1])

    board_2x3 = np.array([[1, 0, 3],
                          [4, 2, 5]])
    zero_position_2x3 = np.array([1, 0])

    solution_node = node.Node.get_node(board_3x3)
    solution_node = solution_node.apply_operator(node.Operator.L)
    solution_node = solution_node.apply_operator(node.Operator.L)
    solution_node = solution_node.apply_operator(node.Operator.D)
    solution_node = solution_node.apply_operator(node.Operator.R)
    solution_node = solution_node.apply_operator(node.Operator.R)
    solution_node = solution_node.apply_operator(node.Operator.U)

    solution = "LLDRRU"

    def test_file_to_node(self):
        read_node = file_io.file_to_node("test_files/4x4_07_00003.txt")
        np.testing.assert_array_equal(self.board, read_node.board)
        np.testing.assert_array_equal(self.zero_position, read_node.zero_position)
        self.assertEqual(None, read_node.parent)
        self.assertEqual(None, read_node.last_operator)

    def test_file_to_node_3x3(self):
        read_node = file_io.file_to_node("test_files/3x3_03_00007.txt")
        np.testing.assert_array_equal(self.board_3x3, read_node.board)
        np.testing.assert_array_equal(self.zero_position_3x3, read_node.zero_position)
        self.assertEqual(None, read_node.parent)
        self.assertEqual(None, read_node.last_operator)

    def test_file_to_node_2x3(self):
        read_node = file_io.file_to_node("test_files/2x3_03_00007.txt")
        np.testing.assert_array_equal(self.board_2x3, read_node.board)
        np.testing.assert_array_equal(self.zero_position_2x3, read_node.zero_position)
        self.assertEqual(None, read_node.parent)
        self.assertEqual(None, read_node.last_operator)

    def test_result_to_file(self):
        path = "test_files/4x4_07_00003_sol.txt"

        file_io.result_to_file(path, self.solution_node)
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.assertEqual("6", lines[0][:-1])
        self.assertEqual(self.solution, lines[1])

    def test_error_to_file(self):
        path = "test_files/solution_error.txt"
        file_io.error_to_file(path)
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.assertEqual("-1", lines[0])

    def test_stats_to_file(self):
        path = "test_files/stats.txt"
        search_statistics = SearchStatistics()
        search_statistics.calculate_solution_length("UUDDLRLRUD")
        search_statistics.increase_visited_states_count(20)
        search_statistics.increase_processed_states_count(15)
        search_statistics.change_max_recursion_depth(5)
        search_statistics.start_runtime_measure()
        time.sleep(0.025)
        search_statistics.stop_runtime_measure()
        file_io.stats_to_file(path, search_statistics)

        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.assertEqual(str(search_statistics.solution_length), lines[0][:-1])
        self.assertEqual(str(search_statistics.visited_states_count), lines[1][:-1])
        self.assertEqual(str(search_statistics.processed_states_count), lines[2][:-1])
        self.assertEqual(str(search_statistics.max_recursion_depth), lines[3][:-1])
        self.assertEqual(str(round(search_statistics.run_time, 3)), lines[4])
