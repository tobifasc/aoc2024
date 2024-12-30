import re

sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
file_input = open("../resources/input05").read()

instructions_raw, updates = file_input.split("\n\n")

instructions = {}

for instruction in instructions_raw.split("\n"):
    before, after = instruction.split("|")
    if before in instructions:
        instructions[before].add(after)
    else:
        instructions[before] = {after}

result = 0
for update in updates.split("\n"):
    i = 1
    update = update.split(",")
    while i < len(update):
        current = update[i]
        previous = set(update[:i])
        if current in instructions and not previous.isdisjoint(instructions[current]):
            break
        elif i == len(update) - 1:
            result += int(update[(len(update) - 1) // 2])
        i += 1

print(result)

        


