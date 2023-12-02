import re

inputs = open("input.txt", 'r')

total = 0
color_regex = r"(\d+)\s(\w+)"
round_regex = r"(\d+)"
# Part 1

for line in inputs:
    color_tups = re.findall(color_regex, line)
    round_number = re.search(round_regex, line).group()
    add = True

    for value, color in color_tups:
        value = int(value)
        if color == "red" and value > 12: add = False
        if color == "green" and value > 13: add = False
        if color == "blue" and value > 13: add = False

    if add:
        total += int(round_number)
print(total)

inputs = open("input.txt", 'r')
# Part 2
total_power = 0

for line in inputs:
    mred, mblue, mgreen = 0, 0, 0
    color_tups = re.findall(color_regex, line)

    add = True

    for value, color in color_tups:
        value = int(value)
        if color == "red":
            mred = max(mred, value)
        if color == "green":
            mgreen = max(mgreen, value)
        if color == "blue":
            mblue = max(mblue, value)

    total = mred * mgreen * mblue
    total_power += total

print(total_power)




