def read_data_to_lists():
    global l1, l2
    l1 = []
    l2 = []
    with open('day_1/input.txt', 'r') as file:
        for line in file:
            l1.append(int(line.split(sep='   ')[0]))
            l2.append(int(line.split(sep='   ')[1]))
    return l1, l2


l1, l2 = read_data_to_lists()

l1_s = sorted(l1)
l2_s = sorted(l2)

dist = 0

for el1, el2 in zip(l1_s, l2_s):
    dist = dist + abs(el1 - el2)
sim_score = 0

for el in l1:
    n = l2.count(el)
    score = int(el) * n
    sim_score = sim_score + score

print(f'Distance = {dist}\nSimilarity score = {sim_score}')
