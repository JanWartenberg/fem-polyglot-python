
def get_input():
    return """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


def parse_line(line):
    parts = line.split(" ")
    try:
        amount = int(parts[1])
    except ValueError:
        print("this should never ever happen")

    if parts[0] == "forward":
        return Point(amount, 0)
    elif parts[0] == "up":
        return Point(0, -amount)
    return Point(0, amount)


def main():
    lines = get_input().split("\n")
    pos = Point(0, 0)

    for line in lines:
        amount = parse_line(line)
        pos.x += amount.x
        pos.y += amount.y

    print(pos)


if __name__ == "__main__":
    main()
