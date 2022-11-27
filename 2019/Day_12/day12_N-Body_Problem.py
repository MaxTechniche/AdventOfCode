input_ = """<x=-4, y=-14, z=8>
<x=1, y=-8, z=10>
<x=-15, y=2, z=1>
<x=-17, y=-17, z=16>"""
import time

known_places = {}

class Moon():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.seen = set()
        self.repeat_found = False
        
    def update(self, ud):
        self.vel['x'] += ud['x']
        self.vel['y'] += ud['y']
        self.vel['z'] += ud['z']
        self.pos['x'] += self.vel['x']
        self.pos['y'] += self.vel['y']
        self.pos['z'] += self.vel['z']
        
    def energy(self):
        potential_energy = sum(abs(val) for val in self.pos.values())
        kinetic_energy = sum(abs(val) for val in self.vel.values())
        return (potential_energy * kinetic_energy)
        
def gcm(numbers):
    print(numbers)
    numbers = [abs(x) for x in numbers]
    numbers.sort()
    numbers.reverse()
    multiple = numbers[0]
    while True:
        for num in numbers:
            if multiple % num != 0:
                multiple *= num
        else:
            return multiple

moons = []

for line in input_.split('\n'):
    line = line[1:-1].split(', ')
    moon = {}
    pos = {}
    vel = {}
    for e in line:
        k, v = e.split('=')
        pos[k] = int(v)
        vel[k] = 0
        moon['pos'] = pos
        moon['vel'] = vel
    moons.append(Moon(pos, vel))

sets_found = False
step = 100
while True:
    moon_update = {}
    for moon in moons:
        current_moon_update = {'x': 0, 'y': 0, 'z': 0}
        for compare_moon in moons:
            if moon == compare_moon:
                continue
            for axis, val in moon.pos.items():
                if val > compare_moon.pos[axis]:
                    current_moon_update[axis] -= 1
                elif val < compare_moon.pos[axis]:
                    current_moon_update[axis] += 1 
        moon_update[moon] = current_moon_update
    
    seen_count = 0
    for moon in moons:
        if moon.repeat_found:
            seen_count += 1
        if seen_count == len(moons):
            sets_found = True
        # print(moon.pos, moon.vel)
    if sets_found:
        fact = []
        for moon in moons:
            fact.append(len(moon.seen))
        print(gcm(fact))
        break
    else:
        for moon in moons:
            if not moon.repeat_found:
                state = ''
                for axis, val in moon.pos.items():
                    state += str(val)
                for axis, val in moon.vel.items():
                    state += str(val)
                if state in moon.seen:
                    moon.repeat_found = True
                else:
                    moon.seen.add(state)
    
    for moon in moons:
        moon.update(moon_update[moon])
    step += 1
    
total_energy = 0
for moon in moons:
    print(moon.pos, moon.vel)
    total_energy += moon.energy()
print(total_energy)

print(gcm([60, 53, 62, 27, 82226, 33, 131, 41]))
# 
# answer = 360689156787864
# 
# import re
# import operator
# from math import gcd
# from functools import reduce
# 
# def cmp(a, b):
    # return (a>b)-(a<b)
# 
# def zip_list(l):
    # return list(zip(*list(l)))
# 
# def lcm(a,b):
    # return a*b//gcd(a,b)
# 
# def parse_input(data):
    # data = [re.findall(r'-?\d+', l) for l in data.splitlines()]
    # data = [[int(v) for v in d] for d in data]
    # return [[d, [0,0,0]] for d in data]
# 
# def dim(moons, i):
    # return [[p[i], v[i]] for p, v in moons]
# 
# def undim(dims):
    # return [zip_list(v) for v in zip_list(dims)]
# 
# def dim_map(f, moons):
    # return map(lambda d: f(dim(moons,d)), range(3))
# 
# def evolve_dim(moons):
    # for mi, m in enumerate(moons): 
        # for o in moons[mi+1:]:
            # d = cmp(o[0], m[0])
            # m[1], o[1] = m[1]+d, o[1]-d
    # for moon in moons: moon[0] += moon[1]
    # return moons
# 
# def evolve(moons):
    # return undim(dim_map(evolve_dim, moons)) 
# 
# def energy(moon):
    # return [sum(map(abs, c)) for c in moon]
# 
# def total_energy(moon):
    # return reduce(operator.mul, energy(moon))
# 
# def system_energy(moons):
    # return reduce(operator.add, map(total_energy, moons))
# 
# def steps_to_loop(dim):
    # i, n = 1, [d[:] for d in dim]
    # while evolve_dim(n) != dim: 
        # i += 1
    # return i
# 
# moons = parse_input(open('day12_input.txt').read())

# for j in range(1000): moons = evolve(moons)
# print(system_energy(moons))

# loops = dim_map(steps_to_loop, moons)
# print(reduce(lcm, loops))