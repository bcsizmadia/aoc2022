from collections import defaultdict

data = open("inputs/day7.txt").readlines()


def parser(data):
    sizes = defaultdict(int)
    directories = []

    for line in data:
        match line.split():
            case [_, _, "/"]:
                directories = []
            case [_, _, ".."]:
                directories.pop()
            case [_, _, elem]:
                directories.append(elem)
            case [elem, _] if elem.isdigit():
                for i in range(len(directories) + 1):
                    path: str = "/" + "/".join(directories[:i])
                    sizes[path] += int(elem)
    return sizes


def part_one(input):
    return sum([elem for elem in parser(input).values() if elem <= 100000])


def part_two(input):
    return min(
        [
            element
            for element in parser(input).values()
            if element >= (30000000 - (70000000 - parser(input)["/"]))
        ]
    )


print("Part One:", part_one([elem.rstrip("\n") for elem in data]))
print("Part Two:", part_two([elem.rstrip("\n") for elem in data]))
