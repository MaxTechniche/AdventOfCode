with open("input.txt") as f:
    input_ = f.read()
    
floor = input_.count('(') - input_.count(')')
print(floor)