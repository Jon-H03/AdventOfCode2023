import re
import pprint

INPUT = open("input.txt", "r")
SYMBOLS = "!?#$%&*+-/=@"


def prob3a(input):
    matrix = []
    for line in input:
        row = list(line)
        matrix.append(row)

    ROWS, COLS = len(matrix), len(matrix[0])-1
    good = []

    def is_adjacent(r, c):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] in SYMBOLS:
                return True
        return False

    for r in range(ROWS):
        c = 0
        while c < COLS:
            if matrix[r][c].isdigit():
                temp = matrix[r][c]
                offset = 1
                while c + offset < COLS and matrix[r][c + offset].isdigit():
                    temp += matrix[r][c + offset]
                    offset += 1

                adjacent = any(is_adjacent(r, c + i) for i in range(offset))
                if adjacent:
                    good.append(int(temp))
                    c += offset - 1
            c += 1
    print(sum(good))

prob3a(INPUT)

INPUT = open("input.txt", "r")
def prob3b(input):
    matrix = []
    for line in input:
        row = list(line)
        matrix.append(row)

    ROWS, COLS = len(matrix), len(matrix[0])-1

    def search_for_nums(r, c):
        unique_numbers = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc].isdigit():
                while nc > 0 and matrix[nr][nc - 1].isdigit():
                    nc -= 1
                digit = ""

                while nc < COLS and matrix[nr][nc].isdigit():
                    digit += matrix[nr][nc]
                    nc += 1
                unique_numbers.add(int(digit))
        if unique_numbers:
            return unique_numbers if len(unique_numbers) == 2 else None
    total = 0
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == "*":
                numbers = search_for_nums(r, c)
                prod = 1
                if numbers:
                    for num in numbers:
                        prod *= num
                    total += prod
    print(total)




prob3b(INPUT)
