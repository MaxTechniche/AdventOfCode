with open('day03.txt') as f:
    input_ = f.read()
    
directions = {'^':(0, 1), 'v':(0, -1), '>':(1, 0), '<':(-1, 0)}

houses = {(0, 0):1}
current_house = (0, 0)
for direction in input_:
    current_house = (current_house[0]+directions[direction][0], 
                     current_house[1]+directions[direction][1])
    if current_house in houses:
        houses[current_house] += 1
    else:
        houses[current_house] = 1
print(len(houses))
    