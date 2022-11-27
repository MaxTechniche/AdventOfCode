with open('day6_input.txt', 'r') as f:
    input_ = f.read().split('\n')
    
orbits = dict()
for orbit in input_:
    orbits[orbit[4:]] = orbit[:3]
    
you_orbit = []
you_found = False
san_orbit = []
san_found = False
memo = dict()
total = 0
for orbit in input_:
    if orbit[4:] == 'YOU':
        you_found = True
    if orbit[4:] == 'SAN':
        san_found = True
    steps = 1
    current_planet = orbit[:3]
    while current_planet in orbits:
        if you_found:
            you_orbit.append(current_planet)
        if san_found:
            san_orbit.append(current_planet)
        steps += 1
        if current_planet in memo:
            total += memo[current_planet] + steps
            memo[orbit] = memo[current_planet] + steps
            break
        else:
            current_planet = orbits[current_planet]
    else:
        memo[orbit] = steps
        total += steps
        memo[current_planet] = 0
    you_found = False
    san_found = False
    
print(total)

previous_planet = you_orbit[-1]
for planet in you_orbit[::-1]:
    if planet not in san_orbit:
        print(you_orbit.index(previous_planet) + san_orbit.index(previous_planet))
        break
    else:
        previous_planet = planet
