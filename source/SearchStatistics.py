import time

from ISearchStatistics import ISearchStatistics


class SearchStatistics(ISearchStatistics):
    def __init__(self):
        self.__solution_length: int = -1
        self.__visited_states_count: int = 0
        self.__processed_states_count: int = 0
        self.__max_recursion_depth: int = 0
        self.__runtime_start: float = 0
        self.__runtime_end: float = 0

    @property
    def solution_length(self):
        return self.__solution_length

    @property
    def visited_states_count(self):
        return self.__visited_states_count

    @property
    def processed_states_count(self):
        return self.__processed_states_count

    @property
    def max_recursion_depth(self):
        return self.__max_recursion_depth

    @property
    def run_time(self):
        return self.__runtime_end - self.__runtime_start

    def calculate_solution_length(self, solution: str):
        self.__solution_length = len(solution)

    def increase_visited_states_count(self, how_much: int):
        self.__visited_states_count += how_much

    def increase_processed_states_count(self, how_much: int):
        self.__processed_states_count += how_much

    def change_max_recursion_depth(self, new_max_depht: int):
        self.__max_recursion_depth = max([new_max_depht, self.__max_recursion_depth])

    def start_runtime_measure(self):
        self.__runtime_start = time.perf_counter() * 1000

    def end_runtime_measure(self):
        end = time.perf_counter() * 1000

        if self.__runtime_start > end:
            return

        self.__runtime_end = end
