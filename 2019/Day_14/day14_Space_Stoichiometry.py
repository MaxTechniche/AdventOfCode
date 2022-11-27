

class Reaction:
    def __init__(self, name, value, ingredients, tier=None):
        self.name = name
        self.value = value
        self.ingredients = ingredients
        if self.ingredients[0][0] == 'ORE':
            self.tier = 1
        else:
            self.tier = tier


with open('Advent Of Code\AOC_2019\day14_input.txt', 'r') as f:
    input_ = f.read().split('\n')


reactions = dict()
for reaction in input_:
    reaction = reaction.split(' => ')
    reaction_output = reaction[1].split(' ')

    val = int(reaction_output[0])
    namee = reaction_output[1]
    ingred = []

    for element in reaction[0].split(', '):
        element = element.split(' ')
        element = element[::-1]
        reaction_element = (element[0], int(element[1]))
        ingred.append(reaction_element)

    new_reaction = Reaction(namee, val, ingred.copy())
    reactions[namee] = new_reaction

leftovers = dict()

fuel_list = []

ore_left = 1000000000000
fuel = 0
while ore_left > 0:

    ore_list = []
    reaction_list = []
    reaction_list.append(('FUEL', 1))
    while len(reaction_list):
        temp_reactions = reaction_list.copy()
        reaction_list = []
        for reaction in temp_reactions:
            if reaction[0] != 'ORE':
                if reaction[0] in leftovers:
                    current_value = leftovers[reaction[0]]
                    value_count = 0
                else:
                    current_value = reactions[reaction[0]].value
                    value_count = 1

                while current_value < reaction[1]:
                    current_value += reactions[reaction[0]].value
                    value_count += 1

                leftovers[reaction[0]] = current_value - reaction[1]

                for ingredient in reactions[reaction[0]].ingredients:
                    reaction_list.append(
                        (ingredient[0], ingredient[1] * value_count))
            else:
                ore_list.append(reaction)

    total_ore = 0
    for base, number in ore_list:
        total_ore += number
    ore_left -= total_ore
    fuel += 1
    if ore_left % 57 == 0:
        print(ore_left)
if ore_left < 0:
    fuel -= 1
    """
    new_fuel = ore_left // total_ore
    
    if ore_left >= 0:
        fuel += ore_left // total_ore
    else:
        while ore_left < 0:
            ore_left += total_ore
            new_fuel -= 1
        fuel += new_fuel
        break

    ore_left %= new_fuel
    for leftover in leftovers:
        leftovers[leftover] *= new_fuel
    fuel_list.append((ore_left, fuel))

    print(ore_left, fuel)
    """

print(fuel)
