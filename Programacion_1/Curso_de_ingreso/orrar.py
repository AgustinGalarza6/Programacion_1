#Crear un programa que solicite 5 números mediante prompt. Calcular la
#suma acumulada y el promedio de los números ingresados.

suma = 0
contador = 0

# Solicitamos 5 números
while contador < 5:
    numero = int(input("Ingresa un número: "))
    suma += numero
    contador += 1

promedio = suma / 5

print("La suma acumulada es:", suma)
print("El promedio es:", promedio)