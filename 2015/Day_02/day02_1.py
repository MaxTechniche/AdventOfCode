with open('day02.txt') as f:
    input_ = [sorted([int(y) for y in x.split('x')]) for x in f.read().split('\n')]
    
total = 0
for box in input_:
    w, h, l = box
    total += sum([3*w*h, 2*w*l, 2*h*l])
    
print(total)
