from time import time
from pprint import pprint

# p0 = 7
# p1 = 2


def find_score(current_player, scores, positions, rolls, memo_wins, current_roll_sum=0):

    check = (
        current_player,
        (scores[0], scores[1]),
        (positions[0], positions[1]),
        (rolls, current_roll_sum)
    )
    if check in memo_wins:
        return memo_wins[check]

    scores = list(scores)
    positions = list(positions)

    if rolls == 3:

        # Increase current players score
        positions[current_player] += current_roll_sum
        positions[current_player] %= 10
        if positions[current_player] == 0:
            positions[current_player] = 10
        scores[current_player] += positions[current_player]

        # if the current player has won, return the score
        if scores[current_player] >= 21:

            if current_player == 0:
                score = (1, 0)
            else:
                score = (0, 1)

            check = (
                (scores[0], scores[1]),
                (positions[0], positions[1]),
                (rolls, current_roll_sum)
            )
            memo_wins[check] = score
            return score

        if current_player == 0:
            current_player = 1
        else:
            current_player = 0
        rolls = 0
        current_roll_sum = 0

    check = (
        current_player,
        (scores[0], scores[1]),
        (positions[0], positions[1]),
        (rolls, current_roll_sum)
    )
    if check in memo_wins:
        return memo_wins[check]

    one = find_score(current_player, scores, positions,
                     rolls+1, memo_wins, current_roll_sum+1)
    two = find_score(current_player, scores, positions,
                     rolls+1, memo_wins, current_roll_sum+2)
    thr = find_score(current_player, scores, positions,
                     rolls+1, memo_wins, current_roll_sum+3)

    w = one[0] + two[0] + thr[0]
    l = one[1] + two[1] + thr[1]

    memo_wins[check] = (w, l)

    return memo_wins[check]


def main():
    t1 = time()
    memo_wins = {}

    print(find_score(0, [0, 0], [4, 8], 0, memo_wins))
    # pprint(memo_wins)
    print((444356092776315, 341960390180808))
    print(find_score(0, [0, 0], [7, 2], 0, memo_wins))

    print("Time:", time() - t1)


main()
