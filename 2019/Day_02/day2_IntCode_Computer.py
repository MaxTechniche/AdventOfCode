
input_original = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

def intCode_reset(original_intCode, desired_value):
    for noun in range(100):
        for verb in range(100):
            print(noun, verb)
            intCode = original_intCode[:]
            intCode[1] = noun
            intCode[2] = verb
            for pos in range(0, len(intCode), 4):
                x = intCode[pos]
                if x == 99:
                    break
                elif x == 1:
                    try:
                        intCode[intCode[pos+3]] = intCode[intCode[pos+1]] + intCode[intCode[pos+2]]
                    except Exception as e:
                        print(e)
                elif x == 2:
                    try:
                        intCode[intCode[pos+3]] = intCode[intCode[pos+1]] * intCode[intCode[pos+2]]
                    except Exception as e:
                        print(e)
                else:
                    break
            if intCode[0] == desired_value:
                print(100 * noun + verb)
                return ('noun:', noun, 'verb:', verb)

print(intCode_reset(input_original, 19690720))
