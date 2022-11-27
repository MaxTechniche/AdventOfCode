with open('day09.txt') as f:
    input_ = f.read().split('\n')
    
input_ = [x.split(' = ')[::-1] for x in input_]
input_ = [[int(x[0]), x[1].split(' to ')] for x in input_]
input_.sort()
print(*input_, sep='\n')

used_cities = input_[0][1]

used_distances = [input_[0][0]]

for d in input_[1:]:
    if d[1][0] in (used_cities[0], used_cities[-1]):
        if d[1][1] not in used_cities:
            if d[1][0] == used_cities[0]:
                used_cities.insert(0, d[1][1])
                used_distances.insert(0, d[0])
            elif d[1][0] == used_cities[-1]:
                used_cities.append(d[1][1])
                used_distances.append(d[0])
    elif d[1][1] in (used_cities[0], used_cities[-1]):
        if d[1][0] not in used_cities:
            if d[1][1] == used_cities[0]:
                used_cities.insert(0, d[1][0])
                used_distances.insert(0, d[0])
            elif d[1][1] == used_cities[-1]:
                used_cities.append(d[1][0])
                used_distances.append(d[0])
    
print(used_distances)
print(sum(used_distances))
        