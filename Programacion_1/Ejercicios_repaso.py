# 1)Desarrollar una funcion que reciba una lista de cadenas y devuelva otra lista con las mismas cadenas ordenadas por su largo de menor a mayor.


# 2)Desarrollar una funcion que reciba una cadena de caracteres, suprima los caracteres repetidos y devuelva la cadena resultante.


# 3)Desarrollar una funcion que reciba una matriz (sopa de letras) y una cadena de caracteres
# si la cadena de caracteres existe en la matriz ya sea horizontal o verticalmente, devolvera True, de lo contrario False.

def revisar_fila(matriz:list, palabra:str, fila:int, columna:int) -> bool:
    largo_palabra = len(palabra) # 3
    largo_maximo = len(matriz[fila]) - columna  # 3
    bandera = True
    for i in range(len(palabra)):       
                # 3              3             r o k               r o k
        if largo_palabra > largo_maximo or palabra[i] != matriz[fila][columna + i]:
            bandera = False
            break
        
    return bandera

def revisar_columna(matriz:list, palabra:str, fila:int, columna:int) -> bool:
    largo_palabra = len(palabra)
    largo_maximo = len(matriz) - fila
    bandera = True
    for i in range(len(palabra)):       
                # 3              3             a k u               a k u
        if largo_palabra > largo_maximo or palabra[i] != matriz[fila + i][columna]:
            bandera = False
            break
        
    return bandera

def encontrar_palabra(matriz:list, palabra:str) -> bool:
    resultado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == palabra[0] and resultado == False:
                resultado = revisar_fila(matriz,palabra,i,j)
                if resultado == False:
                    resultado = revisar_columna(matriz,palabra,i,j)
    
    return resultado 

matriz = [["v", "e", "l", "a"],
        ["a", "r", "o", "k"],
        ["l", "q", "x", "u"]]

palabra_a_buscar = "aku"

# print(encontrar_palabra(matriz,palabra_a_buscar))

# 4)Desarrollar una función que reciba como parámetro una cadena y determine cuántas palabras contiene. La función deberá retornar un entero indicando el número de palabras

# def cantidad_de_palabras(cadena: str) -> int:
#     contador = 0
#     if len(cadena) == 0:
#         return 0
#     else:
#         contador = 1
#         for i in range(len(cadena)):
#             if cadena[i] == ' ':
#                 contador += 1
#         return contador


# Ejemplo de uso 
# print(cantidad_de_palabras("Hola como estas?"))

def limpiar_cadena(cadena:str)->str:
    letra_encontrada = False
    acumulador = ""
    contador_espacios_vacios = 0

    for i in range(len(cadena)-1,-1,-1):
        if cadena[i] == " ":
            contador_espacios_vacios += 1
        else:
            break

    for i in range(len(cadena)-contador_espacios_vacios):
        if cadena[i] != " ":
            letra_encontrada = True
        if letra_encontrada == True:
            acumulador += cadena[i]
            
    return acumulador

def contar_palabras(cadena:str,delimitador:str)->int:
    cadena = limpiar_cadena(cadena)
    if len(cadena) > 0:
        contador_palabras = 1
        for i in range(len(cadena)):
            if cadena[i] == delimitador:
                contador_palabras += 1
    else:
        contador_palabras = 0
    return contador_palabras

# saludo = "   Hola como andas   "
# print(f"{limpiar_cadena(saludo)}.")
# print(contar_palabras(saludo," "))

# 5) Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal
# y en la columna 2 la cantidad. Por ej: cadena = “murcielaguito”

def contar_vocales(palabra:str)->list:
    #[["a",1]
    # ["e",1]
    # ["u",2]
    # ["o",0]]
    matriz = [["a",0],["e",0],["i",0],["o",0],["u",0]]
    for i in range(len(palabra)):
        match palabra[i]:
            case "a":
                matriz[0][1] += 1
            case "e":
                matriz[1][1] += 1
            case "i":
                matriz[2][1] += 1
            case "o":
                matriz[3][1] += 1
            case "u":
                matriz[4][1] += 1

    return matriz

print(contar_vocales("esternocleidomastoideo")) #prohibido!!!