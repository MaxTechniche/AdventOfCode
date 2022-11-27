work = []
min_num = 264793
max_num = 803936

current_number = max_num

while current_number > min_num:
    current_number -= 1
    repeat = False
    reversed_string_num = str(current_number)[::-1]
    if len(str(int(reversed_string_num))) < len(reversed_string_num):
        continue
    for pos in range(1, len(reversed_string_num)):
        if int(reversed_string_num[pos]) > int(reversed_string_num[pos-1]):
            break
        if reversed_string_num.count(reversed_string_num[pos]) == 2:
            repeat = True
    else:
        if repeat:
            work.append(current_number)

print(work)
print(len(work))
