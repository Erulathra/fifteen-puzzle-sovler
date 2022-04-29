import sys
from rich import print

import astar
import file_io as fio
from SearchStatistics import SearchStatistics


def main():
    strategy_parameter = None
    algorithm = None
    start_node_file_path = sys.argv[3]
    solution_file_path = sys.argv[4]
    statistics_file_path = sys.argv[5]

    match sys.argv[1]:
        case "bfs":
            print(f"run bfs with {sys.argv[2:]}")
            return
        case "dfs":
            print(f"run dfs with {sys.argv[2:]}")
            return
        case "astr":
            print(f"run astr with {sys.argv[2:]}")
            if sys.argv[2] == "manh":
                strategy_parameter = astar.manhattan_heuristic
            elif sys.argv[2] == "hamm":
                strategy_parameter = astar.hamming_heuristic

            algorithm = astar.a_star_algorithm

    run_algorithm(algorithm,
                  strategy_parameter,
                  start_node_file_path,
                  solution_file_path,
                  statistics_file_path)


def run_algorithm(strategy,
                  strategy_parameter,
                  start_node_file_path: str,
                  solution_file_path: str,
                  statistics_file_path: str):
    start_node = fio.file_to_node(start_node_file_path)
    search_statistics = SearchStatistics()
    solution_node = strategy(start_node, strategy_parameter, search_statistics)
    if solution_node is not None:
        fio.result_to_file(solution_file_path, solution_node)
    else:
        fio.error_to_file(solution_file_path)
    fio.stats_to_file(statistics_file_path, search_statistics)


if __name__ == '__main__':
    main()
