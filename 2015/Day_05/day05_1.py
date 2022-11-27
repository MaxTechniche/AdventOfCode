with open('day05.txt') as f:
    input_ = f.read().split('\n')
    
def naughty_or_nice(text):
    vowels = 0
    double = False
    previous_letter = text[0]
    nots = ['ab', 'cd', 'pq', 'xy']
    
    if text[0] in 'aeiou':
        vowels += 1
    for letter in range(1, len(text)):
        if text[letter] in 'aeiou':
            vowels += 1
        if previous_letter == text[letter]:
            double = True
        if previous_letter + text[letter] in nots:
            return False
        previous_letter = text[letter]
    
    return (vowels >= 3) and double

count = 0
for string in input_:
    count += naughty_or_nice(string)
    
print(count)