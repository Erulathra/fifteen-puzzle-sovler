from abc import ABC, abstractmethod


class ISearchStatistics(ABC):
    @property
    @abstractmethod
    def solution_length(self) -> int:
        pass

    @property
    @abstractmethod
    def visited_states_count(self) -> int:
        pass

    @property
    @abstractmethod
    def processed_states_count(self) -> int:
        pass

    @property
    @abstractmethod
    def max_recursion_depth(self) -> int:
        pass

    @property
    @abstractmethod
    def run_time(self) -> float:
        pass

    @abstractmethod
    def calculate_solution_length(self, solution: str):
        pass

    @abstractmethod
    def increase_visited_states_count(self, how_much: int):
        pass

    @abstractmethod
    def increase_processed_states_count(self, how_much: int):
        pass

    @abstractmethod
    def change_max_recursion_depth(self, new_max_depth: int):
        pass

    @abstractmethod
    def start_runtime_measure(self):
        pass

    @abstractmethod
    def end_runtime_measure(self):
        pass


class NoneSearchStatistics(ISearchStatistics):
    @property
    def visited_states_count(self) -> int:
        return 0

    @property
    def solution_length(self) -> int:
        return 0

    @property
    def processed_states_count(self) -> int:
        return 0

    @property
    def max_recursion_depth(self) -> int:
        return 0

    @property
    def run_time(self) -> float:
        return 0.

    def calculate_solution_length(self, solution: str):
        pass

    def increase_visited_states_count(self, how_many: int):
        pass

    def increase_processed_states_count(self, how_many: int):
        pass

    def change_max_recursion_depth(self, new_max_depth: int):
        pass

    def start_runtime_measure(self):
        pass

    def end_runtime_measure(self):
        pass
