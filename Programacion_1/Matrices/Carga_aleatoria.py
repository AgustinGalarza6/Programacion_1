def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #for col in range(len(matriz[0]))
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

matriz = inicializar_matriz(3,3,0)
seguir = "s"

print("MATRIZ ANTES DE LA CARGA")
mostrar_matriz(matriz)

#CARGA ALEATORIA
while seguir == "si":
    #Pedimos los indices tanto de la fila como de la columna
    indice_fila = int(input("Ingrese el indice de la fila: ")) 
    #Validar
    indice_columna = int(input("Ingrese el indice de la columna: "))
    #Validar
    
    #Pedimos el numero
    numero = int(input("Ingrese el numero: "))
    #Guardamos el numero en el indice
    matriz[indice_fila][indice_columna] = numero

    # Preguntamos si se desea seguir cargando datos
    seguir = input("¿Desea seguir? (si/no): ")
    if seguir == "no":
        break

mostrar_matriz(matriz)