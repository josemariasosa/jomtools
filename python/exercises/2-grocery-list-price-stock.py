#!/usr/bin/env python
# coding=utf-8

"""
EN:
ES: Hacer un programa al cual el usuario indique un producto y una cantidad.
    El programa debe responder el costo de la mejor combinación de compra.
    Presentar cuántos productos de una tienda y de otra se deben comprar.

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

stock_store_1 = {
    "banana": 1,
    "apple": 30,
    "orange": 3,
    "pear": 1
}

stock_store2 = {
    "banana": 10,
    "apple": 1,
    "orange": 1,
    "pear": 3,
    "tomato": 0
}

product = input('Give me a product: ')

while True:
    quantity = input('The quantity of the given product: ')

    if quantity.isdigit():
        quantity = int(quantity)
        break;
    else:
        print('Quantity must be an integer, try again.\n')

condition_1 = product in prices_store_1.keys()
condition_2 = product in prices_store_2.keys()

if condition_1 and condition_2:
    if prices_store_1[product] >= prices_store_2[product]:
        if stock_store2[product] >= quantity:
            x1 = 0
            x2 = quantity
        else:
            x2 = stock_store2[product]
            if stock_store_1[product] >= (quantity - x2):
                x1 = quantity - x2
            else:
                x1 = stock_store_1[product]
                print('\nNot enough stock in both stores!')
        
    elif prices_store_1[product] < prices_store_2[product]:
        if stock_store_1[product] >= quantity:
            x2 = 0
            x1 = quantity
        else:
            x1 = stock_store_1[product]
            if stock_store2[product] >= (quantity - x1):
                x2 = quantity - x1
            else:
                x2 = stock_store2[product]
                print('\nNot enough stock in both stores!')

    cost = prices_store_1[product] * x1 + prices_store_2[product] * x2
    message = '\nFrom store 1, take: {},'
    message = message + '\nfrom store 2, take: {},\ntotal price: ${}.'
    message = message.format(x1, x2, cost)
    print (message)
    
elif condition_2:
    if stock_store2[product] >= quantity:
        x2 = quantity
    else:
        x2 = stock_store2[product]
        print('\nNot enough stock in both stores!')
        
    cost = prices_store_2[product] * x2
    
    print ('\nFrom store 2, take: {},\ntotal price: ${}.'.format(x2, cost))
    
elif condition_1:
    if stock_store_1[product] >= quantity:
        x1 = quantity
    else:
        x1 = stock_store_1[product]
        print('\nNot enough stock in both stores!')
        
    cost = prices_store_1[product] * x1
    
    print ('\nFrom store 1, take: {},\ntotal price: ${}.'.format(x1, cost))

else:
    print('\nThe product does not exist!')

# ------------------------------------------------------------------------------