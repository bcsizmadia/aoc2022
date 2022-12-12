file = [f.strip() for f in open("inputs/day1.txt").readlines()]

elves = []
elf = 0

for element in file:
    if not element:
        elves.append(elf)
        elf = 0
        continue
    elf += int(element)

print(max(elves))
print(sum(sorted(elves, reverse=True)[:3]))
