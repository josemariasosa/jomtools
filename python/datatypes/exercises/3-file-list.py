#!/usr/bin/env python
# coding=utf-8

"""
EN: 

ES: Listar todos los archivos de la carpeta actual de manera ordenada con el 
tamaño en bytes.
"""
# ------------------------------------------------------------------------------

import os

file_list = os.listdir()

files = []
for file in file_list:
    files.append([file, os.path.getsize(file)])
files.sort(key=lambda x: x[1], reverse=True)
total_size = 0

print('------------------------------')
for file in files:
    print(file[0], '\t\t', file[1])
    total_size += file[1]
print('------------------------------')
print('Total size:            {}'.format(total_size))


# ------------------------------------------------------------------------------
