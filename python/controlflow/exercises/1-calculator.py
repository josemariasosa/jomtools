
while True:
    valor_a = input('Dame un valor A: ')
    if valor_a.isdigit():
        valor_a = int(valor_a)
        break;
    else:
        print('Por favor ingrese un valor entero, intente de nuevo.')

while True:
    valor_b = input('Dame un valor B: ')
    if valor_b.isdigit():
        valor_b = int(valor_b)
        break;
    else:
        print('Por favor ingrese un valor entero, intente de nuevo.')

menu = """
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir
"""
while True:
    print(menu)
    opcion = input('Dame una opcion numerica: ')

    if opcion == "1":
        print('{a} + {b} = {res}'.format(res=valor_a+valor_b,
                                         a=valor_a,
                                         b=valor_b))
        input('Presione enter para continuar.')

    elif opcion == "2":
        print('{a} - {b} = {res}'.format(res=valor_a-valor_b,
                                         a=valor_a,
                                         b=valor_b))
        input('Presione enter para continuar.')

    elif opcion == "3":
        print('{a} * {b} = {res}'.format(res=valor_a*valor_b,
                                         a=valor_a,
                                         b=valor_b))
        input('Presione enter para continuar.')

    elif opcion == "4":
        print('{a} / {b} = {res}'.format(res=valor_a/valor_b,
                                         a=valor_a,
                                         b=valor_b))
        input('Presione enter para continuar.')

    elif opcion == "5":
        print('adios!')
        exit()

    else:
        print("{} no es una opción válida, intente de nuevo".format(opcion))
