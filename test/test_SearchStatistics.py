import time
from unittest import TestCase

import SearchStatistics


class TestSearchStatistics(TestCase):
    search_statistics = SearchStatistics.SearchStatistics()

    def test_solution_length(self):
        solution = "UUDDLRLR"
        self.search_statistics.calculate_solution_length(solution)
        self.assertEqual(8, self.search_statistics.solution_length)

    def test_visited_states_count(self):
        self.search_statistics.increase_visited_states_count(1)
        self.assertEqual(1, self.search_statistics.visited_states_count)
        self.search_statistics.increase_visited_states_count(2)
        self.assertEqual(3, self.search_statistics.visited_states_count)

    def test_processed_states_count(self):
        self.search_statistics.increase_processed_states_count(1)
        self.assertEqual(1, self.search_statistics.processed_states_count)
        self.search_statistics.increase_processed_states_count(1)
        self.assertEqual(2, self.search_statistics.processed_states_count)

    def test_max_recursion_depth(self):
        self.search_statistics.change_max_recursion_depth(10)
        self.assertEqual(10, self.search_statistics.max_recursion_depth)
        self.search_statistics.change_max_recursion_depth(12)
        self.assertEqual(12, self.search_statistics.max_recursion_depth)
        self.search_statistics.change_max_recursion_depth(8)
        self.assertEqual(12, self.search_statistics.max_recursion_depth)

    def test_run_time(self):
        self.search_statistics.start_runtime_measure()
        time.sleep(0.025)
        self.search_statistics.end_runtime_measure()
        self.assertGreaterEqual(self.search_statistics.run_time, 24)
