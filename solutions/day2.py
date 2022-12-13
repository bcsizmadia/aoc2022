with open("inputs/day2.txt") as file:
    lines = file.read().strip().split("\n")

values = [1, 2, 3]
score = 0
scoring = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}


def part_one():
    global score
    for line in lines:
        opponent, me = [scoring[i] for i in line.split()]
        if (me - opponent) % 3 == 1:
            score += 6
        elif me == opponent:
            score += 3
        score += values[me]
    return score


def part_two():
    score = 0
    scoring["X"] = -1
    scoring["Y"] = 0
    scoring["Z"] = 1

    for line in lines:
        opponent, result = [scoring[i] for i in line.split()]
        score += (result + 1) * 3
        score += values[(opponent + result) % 3]
    return score


print("Part One:", part_one())
print("Part Two:", part_two())
