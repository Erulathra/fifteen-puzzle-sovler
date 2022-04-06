from unittest import TestCase

import numpy as np

import file_io
import node


class Test(TestCase):
    board = np.array([[1, 6, 2, 3],
                      [5, 7, 0, 4],
                      [9, 10, 11, 8],
                      [13, 14, 15, 12]])
    zero_position = np.array([2, 1])

    def test_file_to_node(self):
        node = file_io.file_to_node("test_files/4x4_07_00003.txt")
        np.testing.assert_array_equal(self.board, node.board)
        np.testing.assert_array_equal(self.zero_position, node.zero_position)
        self.assertEqual(None, node.parent)
        self.assertEqual(None, node.last_operator)

    def test_result_to_file(self):
        solution = [node.Operator.U,
                    node.Operator.U,
                    node.Operator.D,
                    node.Operator.D,
                    node.Operator.L,
                    node.Operator.R]
        path = "test_files/4x4_07_00003_sol.txt"

        file_io.result_to_file(path , solution)
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.assertEqual("6", lines[0][:-1])
        self.assertEqual("UUDDLR", lines[1])

    def test_error_to_file(self):
        path = "test_files/solution_error.txt"
        file_io.error_to_file(path)
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.assertEqual("-1", lines[0])

    def test_stats_to_file(self):
        path = "test_files/stats.txt"
        solution_length = 10
        number_of_visited_states = 20
        number_of_processed_states = 15
        recursion_depth = 5
        runtime_duration = 3.1456
        file_io.stats_to_file(path, solution_length, number_of_visited_states,
                              number_of_processed_states, recursion_depth, runtime_duration)

        file = open(path, "r")
        lines = file.readlines()
        file.close()
        self.assertEqual(str(solution_length), lines[0][:-1])
        self.assertEqual(str(number_of_visited_states), lines[1][:-1])
        self.assertEqual(str(number_of_processed_states), lines[2][:-1])
        self.assertEqual(str(recursion_depth), lines[3][:-1])
        self.assertEqual(str(round(runtime_duration, 3)), lines[4])
