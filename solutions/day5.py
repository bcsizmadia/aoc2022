def solve(stacks, movement, part_two):
    for _, quantity, _, fromStack, _, toStack in map(str.split, movement):
        quantity, fromStack, toStack = (
            int(quantity),
            int(fromStack) - 1,
            int(toStack) - 1,
        )

        stacks[toStack].extend(stacks[fromStack][-quantity:]) if part_two else stacks[
            toStack
        ].extend(stacks[fromStack][-1 : -quantity - 1 : -1])

        del stacks[fromStack][-quantity:]
    return stacks


def parser(creates):
    stacks = [[] for _ in range((1 + len(creates[0])) // 4)]
    for line in creates[-2::-1]:
        for stackIdx in range((1 + len(creates[0])) // 4):
            if (crate := line[4 * stackIdx + 1]) != " ":
                stacks[stackIdx].append(crate)
    return stacks


file = open("inputs/day5.txt").read().split("\n\n")
creates, movement = map(str.splitlines, file)
print(
    f"Part One: {str().join(stack[-1] for stack in solve(parser(creates), movement, False))}"
)
print(
    f"Part Two: {str().join(stack[-1] for stack in solve(parser(creates), movement, True))}"
)
