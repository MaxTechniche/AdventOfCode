import hashlib

with open('day04.txt') as f:
    input_ = f.read()
    
    
def hashit(input, number):
    return hashlib.md5(bytearray(input, 'utf8') + bytearray(str(number), 'utf8'))

number = 1
x = hashit(input_, number)
while x.hexdigest()[:6] != '000000':
    number += 1
    x = hashit(input_, number) 
    
else:
    print(number)
