'''
Realizar un programa que permita al usuario ingresar 10 números y contar cuántos son positivos y cuántos son negativos. Mostrar los resultados.
contador = 0
contador_pos = 0
contador_neg = 0
while contador < 10:

    numero = int(input('Dame un numero (int): '))
    if numero > 0:
        contador_pos += 1
    else:
        if numero != 0:
            contador_neg += 1

    contador += 1

print(f'Cantidad de positivos: {contador_pos}')
print(f'Cantidad de negativos: {contador_neg}')


Realizar un programa que permita al usuario ingresar números enteros y multiplique todos los números ingresados hasta que se ingrese un número negativo. Mostrar el producto total.

acumulador_multiplicador = 1
while True:
    numero = int(input('Dame un numero (int): '))
    if numero < 1:
        if numero == 0:
            print('Pusiste un cero maquinola...')
            continue 
        break
    
    acumulador_multiplicador = acumulador_multiplicador * numero # acumulador_multiplicador *= numero

print('Multiplicacion de numeros ingresados: ', str(acumulador_multiplicador))


Realizar un programa que permita al usuario ingresar números enteros y calcule el promedio de los números ingresados hasta que se ingrese un número negativo. Mostrar el promedio.

contador = 0
acumulador = 0
promedio = None

while contador >= 0:

    numero = int(input('Dame un numero (int): '))
    if numero < 0:
        break

    contador += 1
    acumulador += numero

promedio = acumulador / contador
print(f'Promedio de numeros ingresados: {round(promedio, 2)}')


Realizar un programa que permita al usuario ingresar números enteros y encuentre el número mayor ingresado, permitiendo al usuario interrumpir el ingreso de datos. Mostrar el número mayor.


flag = True
numero_maximo = None
validar = 's'

while validar == 's' or validar == 'S':

    numero = int(input('Dame un numero (int): '))
    if flag:
        numero_maximo = numero
        flag = False
    else:
        if numero > numero_maximo:
            numero_maximo = numero

    validar = input('Desea continuar? [S] Si - [CUALQUIER TECLA] No: ')
    if validar != 's' and validar != 'S':
        break

print(f'El numero maximo fue: {numero_maximo}')


Realizar un programa que permita al usuario ingresar números enteros y cuente cuántos son pares y cuántos son impares, permitiendo al usuario interrumpir el ingreso de datos. Mostrar los resultados.

flag = True
cantidad_pares = 0
cantidad_impares = 0
validar = 's'

while validar == 's' or validar == 'S':

    numero = int(input('Dame un numero (int): '))
    
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    validar = input('Desea continuar? [S] Si - [CUALQUIER TECLA] No: ')
    if validar != 's' and validar != 'S':
        break

print(f'Cantidad de pares: {cantidad_pares}')
print(f'Cantidad de impares: {cantidad_impares}')
'''
#En el caso de maximos y minimos: 


Bandera_primer_dato = False

contador = 0
max_num = 0
min_num = 0

while contador < 10:
    contador += 1

    num = input("ingrese un numero: ") 

    #ahora gracias a la bandera yo puedo determinar si esta es la primera iteracion, la primera vez que el codigo entra en el bucle
    if Bandera_primer_dato == False:
        #me guardo el primer numero ingresado en ambos, maximos y minimos
        Max_num = num
        Min_num = num
#cambio el valor de la bandera para que el codigo ya no vuelva a entrar en este condicional
        Bandera_primer_dato = True

    #ahora, si no entra en la condicion anterior es porque ya no es el primer dato y ahi busco el maximo y minimo entre todos los numeros que ingresen:
    
    if num < min_num:
        Min_num = num
    if num > max_num:
        Max_num = num
