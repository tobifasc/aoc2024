import re


sample = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
file_input = open("../resources/input03").read()
get_all_pattern = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')
get_nums_pattern = re.compile(r'mul\((\d+),(\d+)\)')

def parse_input(input_str):
    return get_all_pattern.findall(input_str)

input_lst = parse_input(file_input)

enabled = True
result = 0
for item in input_lst:
    if item.startswith("mul"):
        if enabled:
            nums = get_nums_pattern.search(item)
            result += int(nums.group(1)) * int(nums.group(2))

    if item == "don't()":
        enabled = False
    if item == "do()":
        enabled = True

print(result)




