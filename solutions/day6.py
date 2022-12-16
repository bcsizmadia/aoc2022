with open("inputs/day6.txt") as file:
    datastream = file.readline()


def solve(datastream, limit):
    markers = []
    processed = 0

    for char in datastream:
        markers.append(char)
        if len(markers) > limit:
            markers.pop(0)
        processed += 1
        if len(set(markers)) == len(markers) and len(markers) >= limit:
            return processed


print("Part One:", solve(datastream, 4))
print("Part Two:", solve(datastream, 14))
