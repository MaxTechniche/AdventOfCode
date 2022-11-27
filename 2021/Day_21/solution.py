from time import time

# p1 = 7
# p2 = 2


class Player:
    def __init__(self, pos) -> None:
        self.score = 0
        self.pos = pos

    def move(self, dist):
        self.pos += dist
        self.pos %= 10
        if self.pos == 0:
            self.pos = 10

    def inc_score(self):
        self.score += self.pos


class Die:
    def __init__(self) -> None:
        self.value = 0
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        self.value += 1
        if self.value > 100:
            self.value = 1

        return self.value


def main():
    t1 = time()
    p1 = Player(7)
    p2 = Player(2)

    die = Die()

    current_player = p1
    while p1.score < 1000 and p2.score < 1000:
        for _ in range(3):
            current_player.move(die.roll())
        current_player.inc_score()
        if current_player == p1:
            current_player = p2
        else: 
            current_player = p1

    lower_score = min(p1.score, p2.score)
    print(die.rolls)
    print(lower_score * die.rolls)

    print("Time:", time() - t1)


main()
