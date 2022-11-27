import string
import re

with open('day11_1.txt') as f:
    input_ = f.read()
    
alphabet = string.ascii_lowercase

input_ = list(input_)
found = False
while not found:
    x = -1
    while True:
        if input_[x] == 'z':
            input_[x] = 'a'
            x -= 1
        else:
            char = alphabet[alphabet.find(input_[x])+1]
            input_[x] = char
            break
    if re.search('i|o|l', ''.join(input_)):
        continue
    if not re.search(r'(\w)\1.*(\w)\2', ''.join(input_)):
        continue
    for c in range(len(input_)-3):
        if ''.join(input_[c:c+3]) in alphabet:
            print(''.join(input_))
            found = True
            break
