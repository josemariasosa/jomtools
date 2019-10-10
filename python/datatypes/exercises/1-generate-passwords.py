#!/usr/bin/env python
# coding=utf-8

"""
EN:
ES: El script deberá de crear e imprimir una lista de n claves, de longitud m, 
    incluyendo, al menos, uan minúscula, una mayúscula y un dígito.
    Los valores de n y m serán solicitados al usuario y m deberá tener el
    valor de 8 en caso de que el usuario no proporcione ninguno.
"""
# ------------------------------------------------------------------------------

import string
import random

numbers = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
alpha_numeric = lowercase + uppercase + numbers

while True:
    total_keys = input('Give me the total keys to generate: ')
    if total_keys.isdigit():
        total_keys = int(total_keys)
        if total_keys > 0:
            break
    print('A positive integer is requited!')

len_keys = input('Give me the required length for all the keys: ')
if len_keys.isdigit():
    len_keys = int(len_keys)
    if len_keys < 3:
        len_keys = 8
else:
    len_keys = 8

passwords = []
for key in range(total_keys):
    while True:
        password = ''
        for char in range(len_keys):
            password += random.choice(alpha_numeric)
            test_num = False
            test_upp = False
            test_low = False

        for char in password:
            if not test_num:
                if char in numbers:
                    test_num = True
            if not test_upp:
                if char in uppercase:
                    test_upp = True
            if not test_low:
                if char in lowercase:
                    test_low = True

        if all([test_num, test_upp, test_low]):
            passwords.append(password)
            break

for password in passwords:
    print(password)

# ------------------------------------------------------------------------------
