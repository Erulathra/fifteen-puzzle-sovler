from __future__ import annotations

from enum import Enum
import numpy as np

BOARD_SIZE = 4


class Node:

    def __init__(self, board: np.ndarray, zero_position: np.ndarray, parent: Node, last_operator: Operator):
        self.__board = board
        self.__zero_position = zero_position
        self.__parent = parent
        self.__last_operator = last_operator

    def copy(self) -> Node:
        return Node(self.__board, self.__zero_position, self.__parent, self.last_operator)

    def apply_operator(self, operator: Operator) -> Node:
        new_zero_position = self.__zero_position + np.array(operator.value)

        # Check is number out of board
        if new_zero_position[0] >= BOARD_SIZE or new_zero_position[1] >= BOARD_SIZE \
                or new_zero_position[0] < 0 or new_zero_position[1] < 0:
            raise NewPositionIsOutOfBoardException()

        # swap zero with another number
        new_board = self.__board.copy()
        x1, y1 = self.__zero_position
        x2, y2 = new_zero_position
        new_board[y1][x1], new_board[y2][x2] = new_board[y2][x2], new_board[y1][x1]

        # Create new node and return it
        return Node(new_board, new_zero_position, self, operator)

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


class NewPositionIsOutOfBoardException(Exception):
    pass
