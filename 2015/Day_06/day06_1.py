import re

class LightGrid(object):
    def __init__(self, size):
        self.grid = [[False for x in range(size)] for y in range(size)]
        
    def on(self, light):
        x, y = light
        self.grid[x][y] = True
    
    def off(self, light):
        x, y = light
        self.grid[x][y] = False
    
    def toggle(self, light):
        x, y = light
        self.grid[x][y] = not self.grid[x][y]
        
    def lights_on(self):
        total = 0
        for x in self.grid:
            for y in x:
                total += y
        return total

with open('day06.txt') as f:
    input_ = f.read().split('\n')

grid = LightGrid(1000)

for line in input_:
    instruction = re.search('(on|off|toggle)', line)
    lights = re.search('(\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})', line)
    print(instruction[0])
    lights = [(int(lights[1]), int(lights[3])), (int(lights[2]), int(lights[4]))]
    if instruction[0] == 'on':
        c = grid.on
    elif instruction[0] == 'off':
        c = grid.off
    else:
        c = grid.toggle
    for x in range(lights[0][0], lights[0][1]+1):
        for y in range(lights[1][0], lights[1][1]+1):
            c((x, y))
            
print(grid.lights_on())