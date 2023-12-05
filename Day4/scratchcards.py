INPUT = open("input.txt", "r")


def prob4a(input):
    total = 0
    for line in input:
        winning_nums, my_nums = line.split('|')
        winning_nums = winning_nums[9:]

        winning_nums = [int(num) for num in winning_nums.split()]
        my_nums = [int(num) for num in my_nums.split()]

        multiplier = 0
        for num in my_nums:
            if num in winning_nums:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier *= 2
        total += multiplier
    print(total)

#prob4a(INPUT)


#INPUT = open("input.txt", "r")


def prob4b(input):
    scratch_hash = {}
    i = 1
    lines = input.readlines()
    for _ in lines:
        scratch_hash[i] = 1
        i += 1

    current_card = 1
    for line in lines:
        winning_nums, my_nums = line.split('|')
        winning_nums = winning_nums[9:]

        winning_nums = [int(num) for num in winning_nums.split()]
        my_nums = [int(num) for num in my_nums.split()]

        total_nums = 0
        for num in my_nums:
            if num in winning_nums:
                total_nums += 1

        for i in range(1, total_nums+1):
            scratch_hash[current_card+i] += 1*scratch_hash[current_card]

        current_card += 1
    print(sum(scratch_hash.values()))



prob4b(INPUT)