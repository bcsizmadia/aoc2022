from string import ascii_lowercase, ascii_uppercase

with open("inputs/day3.txt") as file:
    lines = file.read().strip().split("\n")

letter = ascii_lowercase + ascii_uppercase
count = 0


def part_one():
    global count
    for line in lines:
        first_half = line[: (len(line) // 2)]
        second_half = line[(len(line) // 2) :]

        for i, c in enumerate(letter):
            if c in first_half and c in second_half:
                count += letter.index(c) + 1
    return count


def part_two():
    count = 0
    for i in range(0, len(lines), 3):
        group = lines[i : (i + 3)]

        for i, c in enumerate(letter):
            if all([c in line for line in group]):
                count += letter.index(c) + 1
    return count


print("Part One:", part_one())
print("Part Two:", part_two())
