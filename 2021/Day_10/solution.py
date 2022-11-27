from time import time

t1 = time()

with open("2021/Day_10/input") as f:
    lines = f.read().splitlines()


total_syntax_score = 0

part_1_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

completion_scores = []

part_2_scores = {')': 1, ']': 2, '}': 3, '>': 4}

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

for line in lines:
    open_brackets = [line[0]]

    for bracket in line[1:]:
        if bracket in brackets.keys():
            open_brackets.append(bracket)
        else:
            last_open_bracket = open_brackets[-1]
            if brackets[last_open_bracket] != bracket:
                total_syntax_score += part_1_scores[bracket]
                break
            else:
                open_brackets = open_brackets[:-1]
    else:
        # Part 2
        score = 0
        for bracket in open_brackets[::-1]:
            score *= 5
            score += part_2_scores[brackets[bracket]]
        completion_scores.append(score)


print("Part 1: " + str(total_syntax_score))

completion_scores.sort()
print("Part 2: " + str(completion_scores[len(completion_scores)//2]))

print("Time:", time() - t1)
