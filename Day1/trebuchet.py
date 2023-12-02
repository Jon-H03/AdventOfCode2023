
# Part 1
total = 0

with open("input.txt", 'r') as f:
    for line in f:
        stack = []
        for c in line:
            if c.isdigit(): stack.append(str(c))
        digit = stack[0] + stack[-1]
        total += int(digit)

print(total)

# Part 2

word_to_num = {"one": 1,
               "two": 2,
               "three": 3,
               "four": 4,
               "five": 5,
               "six": 6,
               "seven": 7,
               "eight": 8,
               "nine": 9}

total = 0

with open("input.txt", 'r') as f:
    for line in f:
        stack = []
        for l in range(len(line)):
            if line[l].isdigit():
                stack.append(str(line[l]))
            for r in range(l, len(line)):
                if r - l > 5:
                    break
                if line[l:r] in word_to_num:
                    stack.append(word_to_num[line[l:r]])
        digit = str(stack[0]) + str(stack[-1])
        total += int(digit)
print(total)
