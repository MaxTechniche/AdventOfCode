from collections import defaultdict
import itertools
import math
import re
from pprint import pprint
from itertools import combinations, combinations_with_replacement, permutations, product
import itertools

HIT_POINTS = 'Hit Points'
DAMAGE = 'Damage'
ARMOR = 'Armor'
COST = 'Cost'
MANA = 'Mana'
HEAL = 'Heal'
WEAPONS = 'Weapons'
RINGS = 'Rings'
TURNS = 'Turns'

boss_input = open('2015/Day_22day22 boss.txt').read().split('\n')
boss = {}
for line in boss_input:
    x, y = line.split(': ')
    boss[x] = int(y)
player = {HIT_POINTS: 50, MANA: 500, ARMOR: 0}

input_ = open('day22 spells.txt').read().split('\n')
spells = defaultdict(dict)
for group in input_:
    group = group.split(',  ')
    group[0] = group[0].split(': ')
    for pair in group[1:]:
        pair = pair.split(': ')
        spells[group[0][1]][pair[0]] = int(pair[1])

pprint(spells)
print(player)
print(boss)

class Game():
    def __init__(self, player, boss, spell_permutation):
        global spells
        self.p_hp = player[HIT_POINTS]
        self.p_mana = player[MANA]
        self.p_armor = player[ARMOR]

        self.b_hp = boss[HIT_POINTS]
        self.b_damage = boss[DAMAGE]

        self.total_mana_used = 0

        self.spells = list(spell_permutation)
        self.shield = 0
        self.poison = 0
        self.recharge=0

    def cast_spell(self, spell):
        if spell == 'Magic Missle':
            self.b_hp -= spells['Magic Missle'][DAMAGE]
        elif spell == 'Drain':
            self.b_hp -= spells['Drain'][DAMAGE]
            self.p_hp += spells['Drain'][HEAL]
        elif spell == 'Shield':
            if self.shield:
                return False
            self.shield = spells['Shield'][TURNS]
        elif spell == 'Poison':
            if self.poison:
                return False
            self.poison = spells['Poison'][TURNS]
        elif spell == 'Recharge':
            if self.recharge:
                return False
            self.recharge = spells['Recharge'][TURNS]
        return True

    def turns(self):
        if self.shield:
            self.p_armor = spells['Shield'][ARMOR]
            self.shield -= 1

        if self.poison:
            self.b_hp -= spells['Poison'][DAMAGE]
            self.poison -= 1

        if self.recharge:
            self.p_mana += spells['Recharge'][MANA]
            self.recharge -= 1  

    def run(self):
        pass

minimum_spent_mana = math.inf
maximum_spent_mana = 0
count = 0

for perm in product(spells, repeat=8):
    count += 1
    game = Game(player, boss, perm)
    if game.run():
        minimum_spent_mana = min(minimum_spent_mana, game.total_mana_used)
        maximum_spent_mana = max(maximum_spent_mana, game.total_mana_used)
        print(minimum_spent_mana)
        print(maximum_spent_mana)
        print(count)
        print(perm)
        print()

print(count)
print(minimum_spent_mana)
print(maximum_spent_mana)