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

        self.test_Node = node.Node.get_node(self.test_board)

    def test_get_node(self):
        test_node = node.Node.get_node(self.test_board)
        np.testing.assert_array_equal(np.array([3, 3]), test_node.zero_position)
        test_node = node.Node.get_node(self.test_board_L)
        np.testing.assert_array_equal(np.array([2, 3]), test_node.zero_position)

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

    def test_hash(self):
        node_one = node.Node.get_node(self.test_board)
        node_two = node.Node.get_node_advanced(self.test_board, node_one, node.Operator.U)
        node_three = node.Node.get_node_advanced(self.test_board_L, node_one, node.Operator.L)

        self.assertEqual(hash(node_one), hash(node_two))
        self.assertNotEqual(hash(node_one), hash(node_three))

    def test_is_goal(self):
        self.assertTrue(self.test_Node.is_goal())

    def test_operator_to_string(self):
        self.assertEqual("L", str(node.Operator.L))
        self.assertEqual("R", str(node.Operator.R))
        self.assertEqual("U", str(node.Operator.U))
        self.assertEqual("D", str(node.Operator.D))
