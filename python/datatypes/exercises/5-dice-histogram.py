
#!/usr/bin/env python
# coding=utf-8

"""
EN: 

ES: Generar un histograma con la frecuencia de resultados de la suma de los
valores resultantes de arrojar dos dados.

2 **
3 ******
4 **********
5 **************
6 *********
7 **********
8 *******************
9 **************
10 *******
11 ******
12 ***
"""
# ------------------------------------------------------------------------------

import random

while True:
    total_turn = input('Give me the total number of dice turn: ')
    if total_turn.isdigit():
        total_turn = int(total_turn)
        if total_turn > 0:
            break
    print('A positive integer is required!')

results = []
dice = [1, 2, 3, 4, 5, 6]
for turn in range(total_turn):
    dice_1 = random.choice(dice)
    dice_2 = random.choice(dice)
    results.append(dice_1 + dice_2)

frequencies = {}
chances = list(range(2,13))
for i in chances:
    frequencies[i] = results.count(i)

for k, v in frequencies.items():
    print(k, v * '*')

# ------------------------------------------------------------------------------
