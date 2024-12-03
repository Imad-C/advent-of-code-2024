from collections import Counter

## Task 1
list_1 = []
list_2 = []

with open("day_1/input.txt", "r") as f:
    for line in f:
        pair = line.strip('\n').split('   ')
        list_1.append(int(pair[0]))
        list_2.append(int(pair[1]))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

total_difference = 0
for v1, v2 in zip(list_1, list_2):
    total_difference += abs(v1 - v2)

print(f'Task 1: {total_difference}') # 2196996

## Task 2
count_dict = Counter(list_2) 

similarity_score = 0
for i in list_1:
    if i in count_dict:
        similarity_score += i * count_dict[i]

print(f'Task 2: {similarity_score}') # 23655822