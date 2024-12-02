# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

numeros_pares = 0
numeros_impares = 0

# Lee el primer número.
numero = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while numero != 0:
    # Verificar si el número es impar.
    if numero % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        numeros_impares += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        numeros_pares += 1
    # Leer el siguiente número.
    numero = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", numeros_impares)
print("Conteo de números pares:", numeros_pares)