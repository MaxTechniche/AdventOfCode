from time import time
from copy import deepcopy

t1 = time()

with open("2021/Day_03/input") as f:
    codes = f.read().splitlines()
    
codes = list(map(list, zip(*codes)))
gamma = ""
epsilon = ""

for x in range(len(codes)):
    if codes[x].count('0') > len(codes[x])/2:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
        
print(int(gamma, 2) * int(epsilon, 2))

print("Part 2")

oxy = deepcopy(codes)
x = 0
bd = 0
while len(oxy[0]) > 1:
    if oxy[x].count('1') >= oxy[x].count('0'):
        num = '1'
    else:
        num = '0'
        
    bin_check_pos = 0
    while bin_check_pos < len(oxy[0]):
        if oxy[x][bin_check_pos] != num:
            # Delete binary number at the checked position from each row
            for n in range(len(oxy)):
                del oxy[n][bin_check_pos]
            bd += 1
        else:
            bin_check_pos += 1
            
    x += 1
            
o = ""
for l in oxy:
    o += l[0]
    
print(int(o, 2))

co2 = deepcopy(codes)
x = 0
bd = 0
while len(co2[0]) > 1:
    if co2[x].count('0') <= co2[x].count('1'):
        num = '0'
    else:
        num = '1'

    bin_check_pos = 0
    while bin_check_pos < len(co2[0]):
        if co2[x][bin_check_pos] != num:
            # Delete binary number at the checked position from each row
            for n in range(len(co2)):
                del co2[n][bin_check_pos]
            bd += 1
        else:
            bin_check_pos += 1

    x += 1

c = ""
for l in co2:
    c += l[0]

print(int(c, 2))
print(int(o, 2) * int(c, 2))

print("Time:", time() - t1)
