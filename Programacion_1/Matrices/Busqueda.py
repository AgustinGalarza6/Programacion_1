matriz = [
    [4,7,1],
    [-2,5,9],
    [5,4,-4]
]

#Buscamos si el numero ingresado se encuentra en la matriz

# numero_ingresado = int(input("Ingrese un numero:"))

# bandera = False

# for fil in range(len(matriz)):
#     for col in range(len(matriz[fil])):#len(matriz[0])
#         if matriz[fil][col] == numero_ingresado:
#             bandera = True
#             break
#     if bandera == True:
#         break

# if bandera == True:
#     print(f"El numero {numero_ingresado} se encontro en la matriz")
# else:
#     print(f"El numero {numero_ingresado} no se encontro en la matriz")
    
#Pedir un numero y contar cuantas veces se repite este numero en mi matriz

numero_ingresado = int(input("Ingrese un numero:"))

cantidad_numeros = 0

for fil in range(len(matriz)):
    for col in range(len(matriz[fil])): #len(matriz[0])
        if matriz[fil][col] == numero_ingresado:
            cantidad_numeros += 1

print(f"El numero {numero_ingresado} se encuentra {cantidad_numeros} veces en la matriz. ")