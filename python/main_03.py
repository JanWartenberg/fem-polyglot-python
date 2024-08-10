from typing import NamedTuple


def get_input():
    return """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


class Thing(NamedTuple):
    Tree = "#"
    Snow = "."


def get_thing(char):
    if char == "#":
        return Thing.Tree
    return Thing.Snow


def main():
    lines = get_input().splitlines()

    parsed_lines = []
    for line in lines:
        parsed_lines.append(list(map(get_thing, line)))

    # print(parsed_lines)
    # print(f"number of lines: {len(parsed_lines)}")
    numCol = len(parsed_lines[0])
    print(f"number of columns: {numCol}")

    tree_count = 0
    for idx, line in enumerate(parsed_lines):
        # print(line[idx*3 % numCol])
        if line[idx*3 % numCol] == Thing.Tree:
            tree_count += 1
    print(tree_count)


if __name__ == "__main__":
    main()
