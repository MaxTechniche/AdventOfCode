import re

with open('day05.txt') as f:
    input_ = f.read().split('\n')
    
def naughty_or_nice(text):
    if re.search(r'(.).\1', text) and re.search(r'(..).*\1', text):
        return True
    return False

count = 0
for string in input_:
    count += naughty_or_nice(string)
    
print(count)