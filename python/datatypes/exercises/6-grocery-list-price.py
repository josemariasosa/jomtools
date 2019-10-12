#!/usr/bin/env python
# coding=utf-8

"""
EN: Generate a script in which the user define a single product he is looking
for, and the answer present in which store that product is cheaper.

ES: Hacer un programa al cual el usuario indique el producto que está buscando
y el programa nos responda en cuál de las dos tiendas podemos localizarlo más 
barado.

    prices_store_1 = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    prices_store_2 = {
        "banana": 6,
        "apple": 1.5,
        "orange": 3,
        "pear": 3,
        "tomato": 1
    }
"""
# ------------------------------------------------------------------------------

prices_store_1 = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

prices_store_2 = {
    "banana": 6,
    "apple": 1.5,
    "orange": 3,
    "pear": 3,
    "tomato": 1
}

product = input('Give me a product: ')

condition_1 = product in prices_store_1.keys()
condition_2 = product in prices_store_2.keys()

if condition_1 and condition_2:
    precio_1 = prices_store_1[product]
    precio_2 = prices_store_2[product]
    
    if precio_1 > precio_2:
        print('Buy the product in store 2!')
    elif precio_1 == precio_2:
        print('Buy the product in the closest store, either one or another!')
    else:
        print('Buy the product in store 1!')
        
elif condition_1:
    print('Buy the product in store 1!')
elif condition_2:
    print('Buy the product in store 2!')
else:
    print('The product does not exist!')

# ------------------------------------------------------------------------------
