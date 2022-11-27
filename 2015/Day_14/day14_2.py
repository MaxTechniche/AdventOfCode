import re


class Reindeer(object):
    def __init__(self, name, speed, stam, rest):
        self.name = name
        self.speed = int(speed)
        self.stam = int(stam)
        self.rest = int(rest)
        self.cycle_distance = int(stam) + int(rest)
        self.points = 0
        self.current_step = 1
        self.current_distance = 0
        
    def __add__(self, x):
        self.points += x
        
    def increase_distance(self):
        self.current_distance += self.speed
        
    def step(self):
        if self.current_step <= self.stam:
            self.increase_distance()
        if self.current_step == self.cycle_distance:
            self.current_step = 1
        else:
            self.current_step += 1
            
    def get_distance(self):
        return self.current_distance
            
        
seconds = 2503

reindeers = []
for line in open('day14.txt'):
    rd = re.match('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    name, speed, stam, rest = rd.group(1, 2, 3, 4)
    reindeers.append(Reindeer(name, speed, stam, rest))
    
for x in range(seconds):
    distance = 0
    furthest_deer = []
    
    for r in reindeers:
        r.step()
        a = r.get_distance()
        if a == distance:
            furthest_deer.append(r)
        elif a > distance:
            furthest_deer = [r]
            distance = a
            
    for r in furthest_deer:
        r += 1
        
max_points = max(x.points for x in reindeers)
print(max_points)
