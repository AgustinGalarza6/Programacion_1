# Desafío: Ingresar 4 números y mostrar el valor mínimo como el máximo ingresado

contador=0
min_numero = float('inf')
max_numero = float('-inf')

while(contador<4):
    print("Ingrese un numero")
    num = int(input())

    if num < min_numero:
        min_numero = num

    elif num > max_numero:
        max_numero = num

    contador+=1

print("ejecuciones: ",contador)
print("el valor min es: ", min_numero)
print("el valor max es: ", max_numero)