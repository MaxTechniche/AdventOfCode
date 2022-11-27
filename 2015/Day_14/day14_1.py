import re

reindeer = {}
for line in open('day14.txt'):
    rd = re.match('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    name, speed, stam, rest = rd.group(1, 2, 3, 4)
    reindeer[name] = list(map(int, (speed, stam, rest)))

                          
def find_max_speed(seconds, reindeer):
    max_distance = 0
    max_deer = None
    for name in reindeer:
        speed, stam, rest = reindeer[name]
        total = (seconds // (stam + rest)) * stam
        leftovers = seconds % (stam + rest)
        leftovers = min(leftovers, stam)
        distance = (total + leftovers) * speed
        if distance > max_distance:
            max_distance = distance
            max_deer = name
    return max_distance

print(find_max_speed(2503, reindeer))
