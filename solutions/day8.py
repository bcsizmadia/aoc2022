from math import prod

inputs = [x.strip() for x in open("inputs/day8.txt").readlines()]

X = len(inputs[0])
Y = len(inputs)
XS = range(1, X - 1)
YS = range(1, Y - 1)


def count(predicate, iterable):
    total = 0
    for i in iterable:
        total += 1
        if not predicate(i):
            break

    return total


def part_one():
    return (X * 2 + Y * 2 - 4) + sum(
        any(
            all(n < inputs[x][y] for n in ns)
            for ns in [
                (inputs[xx][y] for xx in reversed(range(x))),
                (inputs[xx][y] for xx in range(x + 1, X)),
                (inputs[x][yy] for yy in reversed(range(y))),
                (inputs[x][yy] for yy in range(y + 1, Y)),
            ]
        )
        for x in XS
        for y in YS
    )


def part_two():
    return max(
        prod(
            count(lambda n: n < inputs[x][y], ns)
            for ns in [
                (inputs[xx][y] for xx in reversed(range(x))),
                (inputs[xx][y] for xx in range(x + 1, X)),
                (inputs[x][yy] for yy in reversed(range(y))),
                (inputs[x][yy] for yy in range(y + 1, Y)),
            ]
        )
        for x in XS
        for y in YS
    )


print("Part One:", part_one())
print("Part Two:", part_two())
