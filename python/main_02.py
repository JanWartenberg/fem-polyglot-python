from typing import NamedTuple


def get_input():
    return """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


Point = NamedTuple("Point", x=int, y=int)
Line = NamedTuple("Line", point1=Point, point2=Point)


def is_straight(line: Line):
    """ horizontal or vertical """
    return line.point1.x == line.point2.x or line.point1.y == line.point2.y


def parse_point(input_line: str):
    split = input_line.split(",")
    p1 = Point(int(split[0]), int(split[1]))
    return p1


def parse_line(input_line: str):
    split = input_line.split(" -> ")
    p1 = parse_point(split[0])
    p2 = parse_point(split[1])
    return Line(p1, p2)


def main():
    assert is_straight(Line(Point(0, 0), Point(0, 4)))
    assert is_straight(Line(Point(1, 3), Point(0, 3)))
    assert not is_straight(Line(Point(1, 2), Point(3, 4)))

    for input_line in get_input().split("\n"):
        parsed = parse_line(input_line)
        if is_straight(parsed):
            print(parsed)


if __name__ == "__main__":
    main()
