with open('day10.txt') as f:
    input_ = f.read()
    
print(input_)

for _ in range(50):
    previous_input_ = ''
    previous_char = input_[0]
    char_count = 1
    for num in input_[1:]:
        if num == previous_char:
            char_count += 1
        else:
            previous_input_ += str(char_count) + previous_char
            previous_char = num
            char_count = 1
    else:
        previous_input_ += str(char_count) + previous_char
        input_ = previous_input_

    print(len(input_))
    print(input_[:50])
