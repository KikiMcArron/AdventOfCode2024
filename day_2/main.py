safe = 0
with open('day_2/input.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        if all(abs(report[i] - report[i + 1]) < 4 for i in range(len(report) - 1)) and (
                all(report[i] < report[i + 1] for i in range(len(report) - 1)) or
                all(report[i] > report[i + 1] for i in range(len(report) - 1))
        ):
            safe += 1

print(f'There is {safe} safe reports')
