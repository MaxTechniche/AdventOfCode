from time import time
from collections import Counter


def main():
    t1 = time()

    prev_counter = Counter()

    with open("2021/Day_14/input") as f:
        lines = f.read().split('\n\n')
        start = lines[0]
        insertions = [line.split(' -> ') for line in lines[1].splitlines()]
        insertions = {l: r for l, r in insertions}

    for pos in range(len(start)-1):
        prev_counter[start[pos:pos+2]] += 1
    for step in range(40):
        next_counter = Counter()
        for counter in prev_counter:
            l, r = list(counter)
            m = insertions[counter]
            next_counter[l+m] += prev_counter[counter]
            next_counter[m+r] += prev_counter[counter]
        prev_counter = next_counter

    letter_counts = Counter()
    for key, value in prev_counter.items():
        letter_counts[key[0]] += value
    letter_counts[start[-1]] += 1

    print(prev_counter)
    print(letter_counts.most_common())
    print(letter_counts.most_common()[0][-1] -
          letter_counts.most_common()[-1][-1])
    print(sum(letter_counts.values()))
    print('\n')

    print("Time:", time() - t1)


main()
