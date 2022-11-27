from time import time

t1 = time()

with open("2021/Day_05/input") as f:
    lines = f.read().replace(' -> ', ',')
    lines = lines.splitlines()
    
def format_line(line):
    line = list(map(int, line.split(',')))
    line = (tuple(line[:2]), tuple(line[2:]))
    return line

def angle(line):
    if line[0][0] == line[1][0]:
        return 'vertical'
    elif line[0][1] == line[1][1]:
        return 'horizontal'
    else:
        return 'diagonal'

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in lines:
    
    line = format_line(line)
    (x1, y1), (x2, y2) = line
    
    if angle(line) in ['diagonal']:
        
        x_step = (-2 * (x1 - x2 > 0)) + 1
        y_step = (-2 * (y1 - y2 > 0)) + 1

        for s in range(abs(x1 - x2)+1):
            grid[x1][y1] += 1
            x1 += x_step
            y1 += y_step
            
    else:
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                grid[x][y] += 1

points = 0

for row in grid:
    for num in row:
        if num > 1:
            points += 1
        
print(points)
    
print("Time:", time() - t1)
