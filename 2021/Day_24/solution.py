from time import time
from operator import mul, floordiv, add, mod, eq


def inp(number):
    return number


OPERATIONS = {
    'div': floordiv,
    'mul': mul,
    'add': add,
    'mod': mod,
    'eql': eq,
    'inp': inp
}


VALID_MODEL_NUMBERS = set()


def parse(ins):
    ins_ = []
    for instruction in ins:
        instruction = instruction.split()
        for slot in range(len(instruction)):
            if instruction[slot] not in 'wxyz':
                try:
                    instruction[slot] = int(instruction[slot])
                except ValueError:
                    instruction[slot] = OPERATIONS[instruction[slot]]
        ins_.append(instruction)

    return ins_


t2 = time()


def solve(ins, w=None, x=0, y=0, z=0, current_number=''):
    ox, oy, oz = x, y, z
    if z < 0:
        return
    global t2
    for i in range(0, len(ins), 18):
        for w in range(9, 0, -1):
            # print(current_number)
            x, y, z = ox, oy, oz

            x = z % 26
            val = ins[i+4][2]
            if val == 0:
                continue
            z //= val
            val = ins[i+5][2]
            x += val
            if x == w:
                x = 0
            else:
                x = 1
            # x = eq(x, w)
            # x = eq(x, 0)
            y = mul(25, x) + 1
            if y == 1:
                continue
            z *= y
            val = ins[i+15][2]
            y = (w + val) * x
            z += y
            
            solve(ins[i+18:], w, x, y, z, current_number+str(w))

    if len(current_number) == 14:
        if z == 0:
            VALID_MODEL_NUMBERS.add(current_number)
            exit()
        if not x:
            print(current_number)
    if time() - t2 > 1:
        t2 = time()
        print(current_number)
        print('x', x, 'y', y, 'z', z)
        print('')


def main():
    t1 = time()

    with open("2021/Day_24/input") as f:
        ins = f.read().splitlines()

    ins = parse(ins)

    solve(ins)
    print(VALID_MODEL_NUMBERS)

    print("Time:", time() - t1)


main()
