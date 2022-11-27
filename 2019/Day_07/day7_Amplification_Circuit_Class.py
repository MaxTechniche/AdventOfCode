og = [3,8,1001,8,10,8,105,1,0,0,21,46,67,76,101,118,199,280,361,442,99999,3,9,1002,9,4,9,1001,9,2,9,102,3,9,9,101,3,9,9,102,2,9,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,1001,9,2,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,1002,9,5,9,101,5,9,9,1002,9,4,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]
og = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]


class Amp():
    def __init__(self, phase, sequence=og):
        self.phase = phase
        self.sequence = sequence
        self.phase_used = False
        self.four_value = None

    def run(self, input_):
        self.pos = 0
        self.input_ = input_
        while self.pos < len(self.sequence):
            x = str(self.sequence[self.pos])
            while len(x) < 5:
                x = '0' + x
            ones = int(x[-3])
            twos = int(x[-4])
            threes=int(x[-5])
            code = int(x[-2:])

            if code == 99:
                return self.four_value

            if ones == 0:
                try:
                    one_spot = self.sequence[self.pos+1]
                except IndexError:
                    one_spot = None
            else:
                one_spot = self.pos+1

            if twos == 0:
                try:
                    two_spot = self.sequence[self.pos+2]
                except IndexError:
                    two_spot = None
            else:
                two_spot = self.pos+2

            if threes == 0:
                try:
                    three_spot = self.sequence[self.pos+3]
                except IndexError:
                    three_spot = None
            else:
                three_spot = self.pos+3

            self.spots = (0, one_spot, two_spot, three_spot)
            
            self.process_code(code)

    def process_code(self, code):
        print(self.sequence)
        if code == 1:
            self.one()
        elif code == 2:
            self.two()
        elif code == 3:
            self.three()
        elif code == 4:
            self.four()
        elif code == 5:
            self.five()
        elif code == 6:
            self.six()
        elif code == 7:
            self.seven()
        elif code == 8:
            self.eight()

    def one(self):
        self.sequence[self.spots[3]] = self.sequence[self.spots[1]] + \
                                       self.sequence[self.spots[2]]
        self.pos += 4

    def two(self):
        self.sequence[self.spots[3]] = self.sequence[self.spots[1]] * \
                                       self.sequence[self.spots[2]]
        self.pos += 4

    def three(self):
        if self.phase_used:
            self.sequence[self.spots[1]] = self.input_
        else:
            self.sequence[self.spots[1]] = self.phase
            self.phase_used = True
        self.pos += 2

    def four(self):
        if self.sequence[self.spots[1]]:
            self.four_value = self.sequence[self.spots[1]]
        self.pos += 2

    def five(self):
        if self.sequence[self.spots[1]] != 0:
            self.pos = self.sequence[self.spots[2]]
        else:
            self.pos += 3
    
    def six(self):
        if self.sequence[self.spots[1]]:
            self.pos += 3
        else:
            self.pos = self.sequence[self.spots[2]]

    def seven(self):
        if self.sequence[self.spots[1]] < self.sequence[self.spots[2]]:
            self.sequence[self.spots[3]] = 1
        else:
            self.sequence[self.spots[3]] = 0
        self.pos += 4

    def eight(self):
        if self.sequence[self.spots[1]] == self.sequence[self.spots[2]]:
            self.sequence[self.spots[3]] = 1
        else:
            self.sequence[self.spots[3]] = 0
        self.pos += 4
            
from itertools import permutations


input_1 = 0
best_thrust = 0
for combo in permutations([5, 6, 7, 8, 9], 5):
    print(combo)
    amp_list = []
    for phase in combo:
        amp_list.append(Amp(phase, og.copy()))
    combo_score = 0
    x = 0
    output = amp_list[x].run(input_1)
    combo_score += output
    while output:
        if x > 3:
            x = 0
        else:
            x += 1
        if output == True:
            break
        combo_score += output
        output = amp_list[x].run(output)
    
    best_thrust = max(best_thrust, combo_score)
print(best_thrust)
    