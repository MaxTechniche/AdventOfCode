with open('day03.txt') as f:
    input_ = f.read()

class Santa(object):
    DIRECTIONS = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    HOUSES = {(0, 0): 1}
    
    def __init__(self):
        self.current_house = (0, 0)
        
    def update_house(self, direction):
        self.current_house = (self.current_house[0]+self.DIRECTIONS[direction][0],
                              self.current_house[1]+self.DIRECTIONS[direction][1])
        
        if self.current_house in self.HOUSES:
            self.HOUSES[self.current_house] += 1
        else:
            self.HOUSES[self.current_house] = 1
        
    def __len__(self):
        return len(Santa.HOUSES)
    
santa = Santa()
robot_santa = Santa()

santas = (santa, robot_santa)
    
for pos in range(len(input_)):
    santas[pos%2].update_house(input_[pos])
    
print(len(santa))
    