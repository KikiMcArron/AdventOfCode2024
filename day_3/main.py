import re

# Day 3 part 1
result_1 = 0
base_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

with open('day_3/input.txt', 'r') as file:
    data = file.read()
    matches = re.findall(base_pattern, data)
    for el in matches:
        mul = int(el[0]) * int(el[1])
        result_1 += mul
print(result_1)

# Day 3 part 2
search = True
updated_pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
regex = re.compile(updated_pattern)
start = 'do()'
stop = 'don\'t()'
result_2 = 0

with open('day_3/input.txt', 'r') as file:
    data = file.read()
    results = [m.group() for m in regex.finditer(data)]
    for el in results:
        if re.fullmatch(base_pattern, el):
            if search:
                mul = re.findall(base_pattern, el)
                result_2 += int(mul[0][0]) * int(mul[0][1])
        elif el == stop:
            search = False
        elif el == start:
            search = True
print(result_2)
