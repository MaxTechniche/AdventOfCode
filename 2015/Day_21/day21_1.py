from collections import defaultdict
import itertools
import math
import re
from pprint import pprint
from itertools import combinations
import itertools

hit_points = 'Hit Points'
damage = 'Damage'
armor = 'Armor'
cost = 'Cost'

w = 'Weapons'
a = 'Armor'
r = 'Rings'

boss_input = open('AOC_2015\day21.txt').read().split('\n')
boss = {}
for line in boss_input:
    x, y = line.split(': ')
    boss[x] = int(y)
player = {hit_points: 100, damage: 0, armor: 0}

input_ = open('AOC_2015\day21 equipment.txt').read().split('\n\n')
equipment = defaultdict(dict)
all_equipment = {}
for group in input_:
    g = []
    choice = None
    for thing in group.split('\n'):
        thing = re.findall('\w+:? \+\d|\w+', thing)
        if thing[0] in [w, a, r]:
            choice = thing[0]
            continue
        s = {x: int(y) for x, y in zip((cost, damage, armor), thing[1:])}
        equipment[choice][thing[0]] = s
        all_equipment[thing[0]] = s

ec = defaultdict(list)

def multi_combinations(dicts, item_type, x_min, x_max):
    for x in range(x_min, x_max):
        dicts[0][item_type].extend(comb for comb in combinations(dicts[1][item_type], x))
    
for item_type in equipment:
    if item_type == w:
        x_min, x_max = 1, 2
    elif item_type == a:
        x_min, x_max = 0, 2
    elif item_type == r:
        x_min, x_max = 0, 3
    multi_combinations((ec, equipment), item_type, x_min, x_max)

all_combinations = [(x, y, z) for x in ec[w] for y in ec[a] for z in ec[r]]

def player_wins(boss, player, equipment, all_equipment):
    p_hp = player['Hit Points']
    p_damage = player['Damage'] + sum(all_equipment[x]['Damage'] for x in equipment)
    p_armor = player['Armor'] + sum(all_equipment[x]['Armor'] for x in equipment)

    b_hp = boss['Hit Points']
    b_damage = boss['Damage']
    b_armor = boss['Armor']

    while p_hp > 0:
        b_hp -= max(1, (p_damage - b_armor))
        if b_hp <= 0:
            return True
        p_hp -= max(1, (b_damage - p_armor))
    return False

lowest_cost = math.inf

for comb in all_combinations:
    comb = list(itertools.chain.from_iterable(comb))
    c = 0
    for item in comb:
        c += all_equipment[item][cost]
    if player_wins(boss, player, comb, all_equipment):
        lowest_cost = min(lowest_cost, c)

print(lowest_cost)