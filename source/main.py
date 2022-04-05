import sys


def main():
    argv = sys.argv
    match argv[1]:
        case "bfs":
            print(f"run bfs with {sys.argv[2]}")
        case "dfs":
            print(f"run dfs with {sys.argv[2]}")
        case "dfs":
            print(f"run a-star with {sys.argv[2]}")


if __name__ == '__main__':
    main()

