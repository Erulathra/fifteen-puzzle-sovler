from __future__ import annotations

from enum import Enum

import numpy as np


class Node:
    __create_key = object()

    def __init__(self, create_key, board: np.ndarray, zero_position: np.ndarray, parent: Node, last_operator: Operator):
        assert (create_key == Node.__create_key), \
            "You should use get_node method"
        self.__board = board
        self.__board_width = board.shape[1]
        self.__board_height = board.shape[0]
        self.__zero_position = zero_position
        self.__parent = parent
        self.__last_operator = last_operator

    @classmethod
    def get_node(cls, board: np.ndarray):
        return cls.get_node_advanced(board, None, None)

    @classmethod
    def get_node_advanced(cls, board: np.ndarray, parent: Node, last_operator: Operator):
        zero_position = np.ravel(np.asarray(board == 0).nonzero())

        # swap coordinates because np.array has (y, x) but we are using Mathematical coordinates
        x, y = zero_position
        zero_position = np.array([y, x])

        return Node(cls.__create_key, board, zero_position, parent, last_operator)

    def copy(self) -> Node:
        return Node(self.__create_key, self.__board.copy(), self.__zero_position, self.__parent, self.last_operator)

    def apply_operator(self, operator: Operator) -> Node:
        new_zero_position = self.__zero_position + np.array(operator.value)

        # Check is number out of board
        if new_zero_position[0] >= self.__board_height or new_zero_position[1] >= self.__board_width \
                or new_zero_position[0] < 0 or new_zero_position[1] < 0:
            raise NewPositionIsOutOfBoardException()

        # swap zero with another number
        new_board = self.__board.copy()
        x1, y1 = self.__zero_position
        x2, y2 = new_zero_position
        new_board[y1][x1], new_board[y2][x2] = new_board[y2][x2], new_board[y1][x1]

        # Create new node and return it
        return Node(self.__create_key, new_board, new_zero_position, self, operator)

    def get_neighbours(self) -> [Node]:
        neighbours = []
        for operator in [Operator.L, Operator.R, Operator.U, Operator.D]:
            try:
                neighbours.append(self.apply_operator(operator))
            except NewPositionIsOutOfBoardException:
                pass
        return neighbours

    def __eq__(self, other):
        return isinstance(other, Node) and (self.board == other.__board).all() and (
                self.__zero_position == other.__zero_position).all()

    def is_goal(self) -> bool:
        for i in range(self.__board_height):
            for j in range(self.__board_width):
                number = (j + i * self.__board_width + 1) % (self.__board_width * self.__board_height)
                if number != self.__board[i][j]:
                    return False

        return True

    def __hash__(self):
        self.__board.flags.writeable = False
        return hash((self.__board.data.tobytes(), self.__zero_position.data.tobytes()))

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    # Properties
    @property
    def board(self):
        return self.__board

    @property
    def zero_position(self):
        return self.__zero_position

    @property
    def parent(self):
        return self.__parent

    @property
    def last_operator(self):
        return self.__last_operator


class Operator(Enum):
    L = [-1, 0]
    R = [1, 0]
    U = [0, -1]
    D = [0, 1]

    def __str__(self) -> str:
        match self:
            case Operator.L:
                return "L"
            case Operator.R:
                return "R"
            case Operator.U:
                return "U"
            case Operator.D:
                return "D"


class NewPositionIsOutOfBoardException(Exception):
    pass
