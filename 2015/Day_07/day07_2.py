with open('day07_2.txt') as f:
    input_ = f.read().split('\n')
    
input_.sort(key=str.lower)

input_ = [x.split(' -> ') for x in input_]

values = {}
for line in list(input_):
    try:
        line[0] = int(line[0])
        values[line[1]] = line[0]
        input_.remove(line)
    except ValueError:
        pass


for line in list(input_):
    line[0] = line[0].split(' ')
while input_:
    for line in list(input_):
        if len(line[0]) > 1:
            if line[0][1] in values:
                values[line[1]] = ~ values[line[0][1]]
                input_.remove(line)
            elif line[0][1] == 'RSHIFT':
                if line[0][0] in values:
                    values[line[1]] = values[line[0][0]] >> int(line[0][2])
                    input_.remove(line)
            elif line[0][1] == 'LSHIFT':
                if line[0][0] in values:
                    values[line[1]] = values[line[0][0]] << int(line[0][2])
                    input_.remove(line)
            elif line[0][1] == 'AND':
                if line[0][0] in values and line[0][2] in values:
                    values[line[1]] = values[line[0][0]] & values[line[0][2]]
                    input_.remove(line)
            elif line[0][1] == 'OR':
                if line[0][0] in values and line[0][2] in values:
                    values[line[1]] = values[line[0][0]] | values[line[0][2]]
                    input_.remove(line)
            if line[0][1] == 'AND':
                if line[0][2] in values:
                    try:
                        values[line[1]] = int(line[0][0]) & values[line[0][2]]
                        input_.remove(line)
                    except ValueError:
                        pass
        else:
            if line[0][0] in values:
                values[line[1]] = values[line[0][0]]
                input_.remove(line)
    print(*input_, sep='\n')
    print(*values.items(), sep='\n')
