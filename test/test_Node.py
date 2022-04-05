from unittest import TestCase
import node
import numpy as np


class TestNode(TestCase):
    def setUp(self) -> None:
        self.test_board = np.array([[1, 2, 3, 4],
                                    [5, 6, 7, 8],
                                    [9, 10, 11, 12],
                                    [13, 14, 15, 0]])
        self.test_board_L = np.array([[1, 2, 3, 4],
                                      [5, 6, 7, 8],
                                      [9, 10, 11, 12],
                                      [13, 14, 0, 15]])
        self.test_board_U = np.array([[1, 2, 3, 4],
                                      [5, 6, 7, 8],
                                      [9, 10, 11, 0],
                                      [13, 14, 15, 12]])

        self.test_Node = node.Node(self.test_board, np.array([3, 3]), None, None)

    def test_apply_operator(self):
        child_node = self.test_Node.apply_operator(node.Operator.L)
        np.testing.assert_array_equal(self.test_board_L, child_node.board)
        np.testing.assert_array_equal(np.array([2, 3]), child_node.zero_position)
        self.assertEqual(self.test_Node, child_node.parent)
        self.assertEqual(node.Operator.L, child_node.last_operator)

    def test_apply_operator_out_of_board(self):
        self.assertRaises(node.NewPositionIsOutOfBoardException, self.test_Node.apply_operator, node.Operator.R)
        self.assertRaises(node.NewPositionIsOutOfBoardException, self.test_Node.apply_operator, node.Operator.D)

        child_node = self.test_Node.copy()
        for i in range(3):
            child_node = child_node.apply_operator(node.Operator.U)
            child_node = child_node.apply_operator(node.Operator.L)

        self.assertRaises(node.NewPositionIsOutOfBoardException, child_node.apply_operator, node.Operator.U)
        self.assertRaises(node.NewPositionIsOutOfBoardException, child_node.apply_operator, node.Operator.L)
