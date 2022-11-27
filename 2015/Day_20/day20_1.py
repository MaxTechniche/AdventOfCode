input_ = int(open('AOC_2015\day20.txt').read().split('\n')[0])

numbers = [0 for x in range(input_//10+1)]


count = 1
for x in range(1, input_//10+1):
    for num in range(x, input_//10+1, x):
        numbers[num] += x*10
    # print(count)
    count += 1
print(count)
for y in range(len(numbers)):
    if numbers[y] >= input_:
        print(y)
        break

