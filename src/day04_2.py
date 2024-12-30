import re


sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
file_input = open("../resources/input04").read()

input_lst = file_input.split("\n")
#input_lst = sample.split("\n")

def search(x, y):
    possible_paths = [
        [('M', -1, -1), ('S', 1, -1), ('S', 1, 1), ('M', -1, 1)],
        [('M', -1, -1), ('M', 1, -1), ('S', 1, 1), ('S', -1, 1)],
        [('S', -1, -1), ('M', 1, -1), ('M', 1, 1), ('S', -1, 1)],
        [('S', -1, -1), ('S', 1, -1), ('M', 1, 1), ('M', -1, 1)],
    ]
    found = 0
    for possible_path in possible_paths:
        for idx, path in enumerate(possible_path):
            letter, new_x, new_y = path
            new_x += x
            new_y += y
            if new_x >= 0 and new_x < len(input_lst[0]) and new_y >= 0 and new_y < (len(input_lst) - 1):
                if input_lst[new_y][new_x] == letter:
                    if idx == 3:
                        found += 1
                    continue

            break
    return found

result = 0
for y, row in enumerate(input_lst):
    for x, char in enumerate(row):
        if char == 'A':
            result += search(x, y)
print(result)

        


