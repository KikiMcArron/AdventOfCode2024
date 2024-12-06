def is_safe(report):
    return (
            all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
            and (
                    all(report[i] < report[i + 1] for i in range(len(report) - 1)) or
                    all(report[i] > report[i + 1] for i in range(len(report) - 1))
            )
    )


def is_safe_with_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


safe = 0
safe_with_damper = 0

with open('day_2/input.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe += 1
        elif is_safe_with_removal(report):
            safe_with_damper += 1

total_safe = safe + safe_with_damper

print(f'There are {safe} safe reports and {safe_with_damper} safe with Problem Dampener reports what gives '
      f'{total_safe} of total safe reports.')
