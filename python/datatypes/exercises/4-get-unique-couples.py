#!/usr/bin/env python
# coding=utf-8

"""
EN: We have a list L, that each of its elements is a list with 2 elements.
Each element in L representa a couple of data. Some of the data is duplicated.
We would like to get the unique pairs.

ES: Tenemos una lista L, que a su vez contiene listas de 2 elementos, cada par
representa una pareja de datos, sin embargo queremos encontrar los elementos 
únicos de la lista L para no repetir la información. Cómo podemos hacer eso.

    products = [['beer', 7], ['chips', 4], ['water', 2], ['beer', 2],
                ['beer', 7], ['gin', 10], ['water', 2], ['water', 2]]
"""
# ------------------------------------------------------------------------------

products = [
    ['beer', 7],
    ['chips', 4],
    ['water', 2],
    ['beer', 2],
    ['beer', 7],
    ['gin', 10],
    ['water', 2],
    ['water', 2]
]

unique_products = []
for product in products:
    unique_products.append(tuple(product))
unique_products = list(set(unique_products))

print (unique_products)

# ------------------------------------------------------------------------------
