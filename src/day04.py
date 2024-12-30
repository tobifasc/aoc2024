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

def search(x, y):
    possible_paths = [[('M', 0, 1), ('A',0, 2), ('S',0, 3)], [('M',0, -1), ('A',0, -2), ('S',0, -3)],
                      [('M',1, 0), ('A',2, 0), ('S',3, 0)], [('M',-1, 0), ('A',-2, 0), ('S',-3, 0)],
                      [('M',1, 1), ('A',2, 2), ('S',3, 3)], [('M',-1, -1), ('A',-2, -2), ('S',-3, -3)],
                      [('M',1, -1), ('A',2, -2), ('S',3, -3)], [('M',-1, 1), ('A',-2, 2), ('S',-3, 3)]]
    found = 0
    for possible_path in possible_paths:
        for letter, new_x, new_y in possible_path:
            new_x += x
            new_y += y
            if new_x >= 0 and new_x < len(input_lst[0]) and new_y >= 0 and new_y < (len(input_lst) - 1):
                try:
                    if input_lst[new_y][new_x] == letter:
                        if letter == 'S':
                            found += 1
                        continue
                except IndexError:
                    print(f"error at ${new_y}:${new_x}")

            break
    return found

result = 0
for y, row in enumerate(input_lst):
    for x, char in enumerate(row):
        if char == 'X':
            result += search(x, y)
print(result)

        


