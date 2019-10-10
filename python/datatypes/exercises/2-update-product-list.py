#!/usr/bin/env python
# coding=utf-8

"""
EN: 

ES: El script mostrará una tabla de productos con la información de las listas,
con el nombre del producto y el precio (no olvidar dar formato $0.00). El
objetivo será que el usuario inserte un nuevo producto a la tabla, por lo tanto,
se le solicitará un producto y su precio nuevo. El producto se insertará en la
lista de productos, se ordenará de manera alfabética y se imprimirá de nuevo la
tabla.

    products = [['beer', 7], ['chips', 4], ['water', 2]]
"""
# ------------------------------------------------------------------------------

products = [['beer', 7], ['chips', 4], ['water', 2]]

def print_table(products):
    print('------------------------------------------')
    print('     PRODUCTS                PRICE')
    print('------------------------------------------')
    for product in products:
        print(' {}\t\t\t $ {:0.2f}'.format(product[0].title(), product[1]))
    print('------------------------------------------')

print_table(products)

product = []

new_product = input('Give me a new product: ')
product.append(new_product)

while True:
    new_price = input('Give me the new product\'s price: ')
    try:
        new_price = float(new_price)
        product.append(new_price)
        break
    except:
        print('The price must be numeric, please try again!')

products.append(product)
products.sort(key=lambda x: x[0])

print_table(products)


# ------------------------------------------------------------------------------
