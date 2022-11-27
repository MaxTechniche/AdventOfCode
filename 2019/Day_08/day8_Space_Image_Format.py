with open('day8_input.txt', 'r') as f:
    input_ = f.read()
    


def make_layers(input_, w, h):
    layers_ = []
    current_layer = []
    for num in range(0, len(input_), w):
        current_layer.append(input_[num:num+w][:])
        if len(current_layer) == h:
            layers_.append(current_layer[:])
            current_layer.clear()
    return layers_

w = 25
h = 6
layers = make_layers(input_, w, h)

least_0s = w * h
least_os_layer = None
for layer in layers:
    zeros = 0
    ones = 0
    twos = 0
    for line in layer:
        zeros += line.count('0')
        ones += line.count('1')
        twos += line.count('2')
    if zeros < least_0s:
        least_0s = zeros
        least_os_layer = ones * twos

print(least_os_layer)
seen_image = [['2' for num in range(w)] for line in range(h)]

for layer in layers:
    for line in range(len(layer)):
        for number in range(len(layer[line])):
            if seen_image[line][number] == '2':
                seen_image[line][number] = layer[line][number]

zeros = 0
ones = 0
twos = 0
for line in seen_image:
    for num in line:
        if num == '1':
            print('#', end='')
        else:
            print(' ', end='')
        print(' ', end='')
    print()
