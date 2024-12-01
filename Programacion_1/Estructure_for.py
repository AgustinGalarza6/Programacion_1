# Estructura FOR
# Actividades

# 1. Mostrar los números ascendentes desde el 1 al 10

'''
for numeros in range (1, 11):
    print(numeros)
'''

# 2. Mostrar los números descendentes desde el 10 al 1

'''
for i in range (10, 0, -1):
    print (i)

Cuando usas range(10, 0, -1), estás especificando lo siguiente:

start es 10, así que la secuencia comienza en 10.
stop es 0, pero este valor no está incluido en la secuencia final.
step es -1, lo que significa que la secuencia disminuirá en lugar de aumentar.

'''

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número
# ingresado.

'''
numero_ingresado = int(input("Ingresa un numero: "))
for i in range (0, numero_ingresado + 1): # Agregamos el +1 porque sino no llega al numero inmgresado, solo imprime hasta el numero anterior
    print(i)
'''

# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
# ejemplo si se ingresa el numero 5:
# 5 x 0 = 0
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 …

'''
numero_ingreso = int(input("Ingresa un numero: ")) #10
for i in range (0, numero_ingreso + 1):
    print(f"{numero_ingreso} x {i} = {numero_ingreso * i}")
'''

# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
# número 0. Mostrar la suma y el promedio de todos los números.

'''
acumulador_suma = 0
cantidad_ingresos = 0

for i in range (10)
    numero_ingresado_usuario = int(input("Ingresa un numero: "))
    if numero_ingresado_usuario == 0:
        break
        
    acumulador_suma += numero_ingresado_usuario
    cantidad_ingresos += 1

#INFORMES
print(f"La suma de todos los numeros es: {acumulador_suma}")
print(f"El promedio de todos los numeros es: {acumulador_suma / cantidad_ingresos}")
'''


# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

'''
for i in range (1, 11):
    if i % 3 == 0:
        print(i)
'''

# 7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
'''
for i in range(50)
    if i % 2 == 0:
        print(i)
'''

# 8. Realizar un programa que permita mostrar una pirámide de números. Por
# ejemplo: si se ingresa el numero 5, la salida del programa será la
# siguiente: (ver grafico en el campus)

'''
numero_ingresado = int(input("Ingresa un número: "))
numero_str = ""
for i in range(1, numero_ingresado + 1):
    numero_str += str(i)
    print(numero_str) 

'''


# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
# el número ingresado. Mostrar la cantidad de divisores encontrados.

'''
numero_ingresado = int(input("Ingresa un número: "))
contador_divisores = 0

for i in range(1, numero_ingresado + 1):
    if numero_ingresado % i == 0:
        contador_divisores += 1  # Incrementar el contador
        print(i)  # Mostrar el divisor

print("Cantidad de divisores encontrados:", contador_divisores)

'''

# 10.Ingresar un número. Determinar si el número es primo o no.
'''
divisores = 0

numero = int(input("Ingresa un número: "))
for i in range (1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("Es primo")
else:
    print("No es primo")
'''


# 11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
# número ingresado. Informar cuántos números primos se encontraron.

contador_de_numeros_primos = 0

numero = int(input("Ingresa un número: "))
for i in range (1, numero + 1):
    print(i)
    if i < 2:
        print("No es primo")
    elif (i == 2) or (i == 3):
        print("Es primo")
        contador_de_numeros_primos += 1
    elif i % 2 == 0:
        print("No es primo, es compuesto")
    else:
        print("Es primo")
        contador_de_numeros_primos += 1

print("Numeros primos encontrados:", contador_de_numeros_primos)