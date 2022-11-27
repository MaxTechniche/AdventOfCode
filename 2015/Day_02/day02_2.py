with open('day02.txt') as f:
    input_ = [sorted([int(y) for y in x.split('x')]) for x in f.read().split('\n')]
    
total = 0
for box in input_:
    w, h, l = box
    total += 2*(w+h) + w*h*l
    
print(total)
