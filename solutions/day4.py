with open("inputs/day4.txt") as file:
    lines = file.read().strip().split("\n")

count = 0
count2 = 0

for line in lines:
    elves = line.split(",")
    ranges = [list(map(int, elf.split("-"))) for elf in elves]

    start1, end1 = ranges[0]
    start2, end2 = ranges[1]

    if ((start1 <= start2) and (end1 >= end2)) or (
        (start1 >= start2) and (end1 <= end2)
    ):
        count += 1

    if not ((end1 < start2) or (start1 > end2)):
        count2 += 1

print("Part One:", count)
print("Part Two:", count2)
