og = [3,8,1001,8,10,8,105,1,0,0,21,46,67,76,101,118,199,280,361,442,99999,3,9,1002,9,4,9,1001,9,2,9,102,3,9,9,101,3,9,9,102,2,9,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,1001,9,2,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,1002,9,5,9,101,5,9,9,1002,9,4,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]

og = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def intCode_compute(original_intCode, input_, phase_setting):
    intCode = original_intCode[:]
    pos = 0
    used_input_one = False
    while pos < len(intCode):
        x = intCode[pos]
        x = str(x)
        while len(x) < 5:
            x = '0' + x
        one = int(x[2])
        two = int(x[1])
        three = int(x[0])
        x = int(x[3:])
        if x == 99:
            return(intCode, False)
            break
        if not one:
            one_spot = intCode[pos+1]
        else:
            one_spot = pos+1
        if not two:
            two_spot = intCode[pos+2]
        else:
            two_spot = pos+2
        if not three:
            three_spot = intCode[pos+3]
        else:
            three_spot = pos+3


        if x == 1:
            intCode[three_spot] = intCode[one_spot] + intCode[two_spot]
            pos += 4

        elif x == 2:
            intCode[three_spot] = intCode[one_spot] * intCode[two_spot]
            pos += 4
        elif x == 3:
            if used_input_one:
                intCode[one_spot] = input_
            else:
                intCode[one_spot] = phase_setting
                used_input_one = True
            pos += 2
        elif x == 4:
            if intCode[one_spot] != 0:
                return (intCode, intCode[one_spot])
            pos += 2
        elif x == 5:
            if intCode[one_spot]:
                pos = intCode[two_spot]
            else:
                pos += 3
        elif x == 6:
            if not intCode[one_spot]:
                pos = intCode[two_spot]
            else:
                pos += 3
        elif x == 7:
            if intCode[one_spot] < intCode[two_spot]:
                intCode[three_spot] = 1
            else:
                intCode[three_spot] = 0
            pos += 4
        elif x == 8:
            if intCode[one_spot] == intCode[two_spot]:
                intCode[three_spot] = 1
            else:
                intCode[three_spot] = 0
            pos += 4
        else:
            break


from itertools import permutations

combo_list = []
# for combo in permutations([0,1,2,3,4], 5):
    # for combo2 in permutations([5,6,7,8,9], 5):
        # combo_list.append(combo + combo2)
        # 
# combo_list.clear()
# for combo2 in permutations([5,6,7,8,9], 5):
    # combo_list.append(combo2)
combo_list.clear()
for combo in permutations([5, 6, 7, 8, 9], 5):
    combo_list.append(combo)

best_thrust = 0

from copy import deepcopy
for combo in combo_list:
    intCode_list = [deepcopy(og) for _ in range(5)]
    combo_score = 0
    phase_1 = combo[0]
    input_1 = 0 #87138
    next_input = intCode_compute(intCode_list[0], input_1, phase_1)
    intCode_list[0] = next_input[0]
    input_recieved = True
    current_amp = 0
    print(combo)
    while input_recieved:
        if current_amp < 4:
            current_amp += 1
        else:
            current_amp =0
        next_input = intCode_compute(intCode_list[current_amp], next_input[1], combo[current_amp])
        intCode_list[current_amp] = next_input[0]
        input_recieved = next_input[1]
        #print(next_input[1])
    best_thrust = max(best_thrust, next_input[1])
    print(best_thrust)
print(best_thrust)
