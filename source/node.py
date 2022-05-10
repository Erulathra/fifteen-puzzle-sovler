from __future__ import annotations

from enum import Enum

import numpy as np


class Node:
    __create_key = object()
    _operator_dict = {"L": np.array([-1, 0]),
                      "R": np.array([1, 0]),
                      "U": np.array([0, -1]),
                      "D": np.array([0, 1])}
    _target_board = None

    def __init__(self, create_key, board: np.ndarray, zero_position: np.ndarray, parent: Node, last_operator: str):
        assert (create_key == Node.__create_key), \
            "You should use get_node method"
        self._board = board
        self._board.flags.writeable = False
        self._board_width = board.shape[1]
        self._board_height = board.shape[0]
        self._zero_position = zero_position
        self._parent = parent
        self._last_operator = last_operator

        if parent is not None:
            self._depth = parent.depth + 1
        else:
            self._depth = 0

    @classmethod
    def get_node(cls, board: np.ndarray):
        return cls.get_node_advanced(board, None, None)

    @classmethod
    def get_node_advanced(cls, board: np.ndarray, parent: Node, last_operator: str):
        zero_position = np.ravel(np.asarray(board == 0).nonzero())

        # swap coordinates because np.array has (y, x) but we are using Mathematical coordinates
        x, y = zero_position
        zero_position = np.array([y, x])

        return Node(cls.__create_key, board, zero_position, parent, last_operator)

    def copy(self) -> Node:
        return Node(self.__create_key, self._board.copy(), self._zero_position, self._parent, self.last_operator)

    def apply_operator(self, operator: str) -> Node:
        new_zero_position = self._zero_position + Node._operator_dict[operator]

        # Check is number out of board
        if new_zero_position[0] >= self._board_height or new_zero_position[1] >= self._board_width \
                or new_zero_position[0] < 0 or new_zero_position[1] < 0:
            raise NewPositionIsOutOfBoardException()

        # swap zero with another number
        new_board = self._board.copy()
        x1, y1 = self._zero_position
        x2, y2 = new_zero_position
        new_board[y1][x1], new_board[y2][x2] = new_board[y2][x2], new_board[y1][x1]

        # Create new node and return it
        return Node(self.__create_key, new_board, new_zero_position, self, operator)

    def get_neighbours(self, order: str = None) -> list[Node]:
        if order is None:
            order = "LRUD"

        neighbours = []
        order = self.remove_prohibited_operators(order)

        for operator in order:
            neighbours.append(self.apply_operator(operator))

        return neighbours

    def remove_prohibited_operators(self, order: str) -> str:
        if self.zero_position[1] == 0:
            order = order.replace('U', '')
        elif self.zero_position[1] >= self._board_height - 1:
            order = order.replace('D', '')
        if self.zero_position[0] == 0:
            order = order.replace('L', '')
        elif self.zero_position[0] >= self._board_width - 1:
            order = order.replace('R', '')
        return order

    def __eq__(self, other):
        return (self.board == other._board).all()

    def is_goal(self) -> bool:
        return (self._board == self.target_board).all()

    @property
    def target_board(self):
        if Node._target_board is None or self._target_board.shape != Node._target_board.shape:
            Node._target_board = self._create_target_board()
        return Node._target_board

    def _create_target_board(self):
        result = np.zeros((self._board_width, self._board_height))
        for i in range(self._board_height):
            for j in range(self._board_width):
                number = (j + i * self._board_width + 1) % (self._board_width * self._board_height)
                result[i][j] = number

        return result

    @property
    def path(self) -> str:
        node = self
        result = ""
        while node.parent is not None:
            result += node.last_operator
            node = node.parent
        return result[::-1]

    @property
    def depth(self) -> int:
        return self._depth

    def __hash__(self):
        return hash(self._board.tobytes()) + hash(self.depth) + hash(self.last_operator)

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    # Properties
    @property
    def board(self):
        return self._board

    @property
    def zero_position(self):
        return self._zero_position

    @property
    def parent(self):
        return self._parent

    @property
    def last_operator(self):
        return self._last_operator


class NewPositionIsOutOfBoardException(Exception):
    pass
