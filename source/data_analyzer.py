# This file is a huge mess, and I know about it.

import sys
from statistics import mean

import numpy as np
from matplotlib import pyplot


def main():
    pyplot.rcParams["figure.figsize"] = (8, 5)
    data_dict = extract_data_to_dict()
    general_data = extract_general_data_to_dict()

    plot_general_data()


def plot_general_data():
    general_data = extract_general_data_to_dict()

    dfs = []
    bfs = []
    astr = []

    for data in general_data.values():
        if data[0] == "astr":
            astr.append(data)
        if data[0] == "bfs":
            bfs.append(data)
        if data[0] == "dfs":
            dfs.append(data)

    # solution len
    for i, parameter in enumerate(["Średnia długość rozwiązania", "Średnia ilość stanów odwiedzonych",
                                   "Średnia ilość stanów przetoworzonych", "Średnia maksymalna głębokość rekursji",
                                   "Średni czas działania algorytmu"]):
        for j, (algorithm, name) in enumerate([(bfs, "BFS"), (dfs, "DFS"), (astr, "A*")]):
            datax = []
            datay = []
            for k in algorithm:
                datax.append(k[2])
                datay.append(mean(k[i + 3]))

            pos = (0.9 / 3) * j - 0.15
            pyplot.bar(np.array(datax) - pos, datay, label=name, width=0.3, align="edge")

        if i in [1,2,4]:
            pyplot.yscale('log')

        pyplot.legend()
        pyplot.xlabel("Głębokość rozwiązania")
        pyplot.ylabel(parameter)
        pyplot.show()


def extract_data_to_dict():
    data_dict = {}
    path = sys.argv[1]
    with open(path, "r") as file:
        for line in file.readlines():
            line = line.split(" ")
            if line[2] + line[3] + line[0] not in data_dict.keys():
                data_dict[line[2] + line[3] + line[0]] = (line[2], line[3], int(line[0]), [], [], [], [], [])

            data = data_dict[line[2] + line[3] + line[0]]
            line_to_data(data, line)
    return data_dict


def extract_general_data_to_dict():
    data_dict = {}
    path = sys.argv[1]
    with open(path, "r") as file:
        for line in file.readlines():
            line = line.split(" ")
            if line[2] + line[0] not in data_dict.keys():
                # strategy,  parameter, depth, solution length, visited, processed, max recursion, runtime
                data_dict[line[2] + line[0]] = (line[2], "General", int(line[0]), [], [], [], [], [])

            data = data_dict[line[2] + line[0]]
            line_to_data(data, line)
    return data_dict


def line_to_data(data, line):
    data[3].append(int(line[4]))
    data[4].append(int(line[5]))
    data[5].append(int(line[6]))
    data[6].append(int(line[7]))
    data[7].append(float(line[8]))


if __name__ == "__main__":
    main()
