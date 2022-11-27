from time import time
from ast import literal_eval as le
from math import floor, ceil


class Number:
    def __init__(self, value=None, parent=None, left=None, right=None, depth=0):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth

    def explode(self):
        if self.parent.left == self:
            child = 'left'
        else:
            child = 'right'
        n = Number(value=0, parent=self.parent, depth=self.depth)

        # Left
        current = self
        while current.parent:
            if current.parent.left == current:
                current = current.parent
            else:
                current = current.parent.left
                while not current.value:
                    if current.value == 0:
                        break
                    current = current.right
                current.value += self.left.value
                break

        # Right
        current = self
        while current.parent:
            if current.parent.right == current:
                current = current.parent
            else:
                current = current.parent.right
                while not current.value:
                    if current.value == 0:
                        break
                    current = current.left
                current.value += self.right.value
                break

        if child == 'left':
            self.parent.left = n
        elif child == 'right':
            self.parent.right = n

    def split(self):
        # create next node
        l = Number(floor(self.value/2), parent=self.parent)
        r = Number(ceil(self.value/2), parent=self.parent)

        if self.parent.left == self:
            self.parent.left = Number(
                parent=self.parent, left=l, right=r, depth=self.depth)
        elif self.parent.right == self:
            self.parent.right = Number(
                parent=self.parent, left=l, right=r, depth=self.depth)

    def check_for_explode(self):
        if self.left:
            if self.left.check_for_explode():
                return True
        if self.right:
            if self.right.check_for_explode():
                return True

        if self.depth >= 4 and type(self.value) != int:
            self.explode()
            return True

    def check_for_split(self):
        if self.left:
            if self.left.check_for_split():
                return True
        if self.right:
            if self.right.check_for_split():
                return True

        if type(self.value) == int:
            if self.value > 9:
                self.split()
                del self
                return True

    def red(self):
        if self.check_for_explode():
            return True

        if self.check_for_split():
            return True

    def restructure(self, parent=None, depth=0):
        self.depth = depth
        self.parent = parent
        if self.left:
            self.left.restructure(parent=self, depth=depth+1)
        if self.right:
            self.right.restructure(parent=self, depth=depth+1)

    def magnitude(self):
        if type(self.value) == int:
            return self.value
        else:
            return self.left.magnitude()*3 + self.right.magnitude()*2

    def __str__(self):
        if self.value == 0:
            return str(self.value)
        if not self.value:
            return '[' + str(self.left) + ',' + str(self.right) + ']'
        return str(self.value)


def parse(number, depth=0):

    l, r = number
    if type(l) is list:
        l = parse(l, depth+1)
    else:
        l = Number(l)
    if type(r) is list:
        r = parse(r, depth+1)
    else:
        r = Number(r)
    number = Number(left=l, right=r, depth=depth)
    number.left.parent = number
    number.right.parent = number
    return number


def main():
    t1 = time()

    with open("2021/Day_18/input") as f:
        ns = f.read().splitlines()

    prev_n = parse(le(ns[0]))
    for n in ns[1:]:
        n = parse(le(n))
        next_n = Number(left=prev_n, right=n)
        prev_n = parse(le(str(next_n)))
        while prev_n.red():
            prev_n = parse(le(str(prev_n)))

    print(prev_n)
    print(prev_n.magnitude())

    total = 0
    for n1 in range(len(ns)):
        n1n = parse(le(ns[n1]))
        for n2 in range(len(ns)):
            if n1 == n2:
                continue
            n2n = parse(le(ns[n2]))
            n = Number(left=n1n, right=n2n)
            # Restructure
            # n.restructure()
            n = parse(le(str(n)))
            while n.red():
                # n.restructure()
                n = parse(le(str(n)))
                # print(n)
            # print(n1n)
            # print(n2n)
            # print(n)
            # print('')
            total = max(total, n.magnitude())

    print(total)

    print("Time:", time() - t1)


main()
