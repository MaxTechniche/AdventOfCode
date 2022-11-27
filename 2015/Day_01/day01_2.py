with open("day01.txt") as f:
    input_ = f.read()
    
floor = 0
for char in range(len(input_)):
    if input_[char] == ')':
        floor -= 1
    else:
        floor += 1
    if floor < 0:
        print(char+1)
        break
