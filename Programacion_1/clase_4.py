# las litas en python puede almacenar cualquier tipo de dato
# Las listas son colecciones de datos.
# pero acostumbrense a trabajar listas para un solo tipo de dato en concreto
# Lista [numeros]
# Lista [caracteres]
# etc
# El indice de las listas arranca siempre en 0 (si tenes 6 datos, el indice de la lista es 5)

#------------------------------------------------------------------------------

# Ejemplo para extraer un dato de una lista
# mi_lista = [1, 2, 3, 4, 5]
# print (mi_lista[2]) (nos muestra el "3")

# lista = [1, 2, 3, 4, 5]
# lista[3] = 22
# lista = [1, 2, 3, 22, 5]

#------------------------------------------------------------------------------

# para trabajar listas y mostrar los elementos tenemos que hacer:

# lista = [1, 2, 3, 4, 5]
# for elemento in lista:
#     print(elemento)

# lista = [1, 2, 3, 4, 5]
# for i in range(4)
#     print(lista[i])

# largo_de_mi_lista = len (mi_lista)
# for i in range(largo_de_mi_lista):
#     print(mi_lista[i])

# for num in mi_lista
#     print(num)

# for num in mi_lista
#     print(num, end=" ") (para imprimir los valores sin salto de linea)

#------------------------------------------------------------------------------

# como pasar un str iterable a una lista
# str = "hola mundo"
# lista = list(str)
# print (lista)

# como convertir un rango (range) a lista

# mi_rango = range(5) (Genera un objeto iterable [0, 1, 2, 3, 4])
# mi_lista = list(mi_rango)
# print(mi_lista)

#------------------------------------------------------------------------------

# como unir listas?

# mi_lista = [1, 2, 3, 4, 5]
# otra_lista = [6, 7, 8, 9, 10]
# resultado = mi_lista + otra_lista
# print (resultado)

# mi_lista = [1, 2, 3, 4, 5]
# mi_lista += [6, 7]
# print (mi_lista)

#------------------------------------------------------------------------------

# agregar datos segun ingrese el usuario
# mi_lista = []
# numero_ingresado = int(input("Ingresa un numero: "))
# mi_lista += [numero_ingresado]
# print (mi_lista)

#------------------------------------------------------------------------------

# def cargar_lista_secuencialmente(lista:list)-> None:
#     '''
#     Esta funcion carga los datos de forma secuencial 5 veces
#     reemplaza los None por los numeros que ingrese el usuario
#     '''
#     for i in range(len(lista)):
#         numero_ingresado = int(input("Ingresa un numero: "))
#         lista[i] = numero_ingresado

# lista = [None] * 5
# print(lista)
# cargar_lista_secuencialmente(lista)
# print(lista)

#------------------------------------------------------------------------------

# def append_algoritmo(lista:list, elemento:int)-> None:
#     '''
#     Esta funcion agrega un elemento al final de la lista
#     '''
#     numero_ingresado = int(input("Ingresa un numero que desea agregar: "))
#     while numero_ingresado < 0:
#         print("Ingresa un numero positivo")
#         numero_ingresado = int(input("Ingresa un numero nuevamente que desee agregar: "))
#     lista += [numero_ingresado]

# mi_lista = [1, 2, 3]
# append_algoritmo(mi_lista, 4)
# print(mi_lista)

#------------------------------------------------------------------------------

# def cargar_lista_aleatoriamente(lista:list)-> None:
#     while True:
#         indice_ingresado = int(input("Ingrese el indice a modificar: "))
#         while indice_ingresado < 0 or indice_ingresado >= len(lista):
#             print("Ingresa un indice valido")
#             indice_ingresado = int(input("Ingresa un indice nuevamente: "))
        
#         nota_ingresada = int(input("Ingresa una nota: "))
#         while nota_ingresada < 0 or nota_ingresada > 10:
#             print("Ingresa una nota entre 0 y 10")
#             nota_ingresada = int(input("Ingresa una nota nuevamente: "))
#         # Asignamos el dato a la list
#         lista[indice_ingresado] = nota_ingresada

#         respuesta = input("¿Desea cargar otra nota? (s/n): ")
#         if respuesta == "n":
#             break

# mi_lista = [1, 2, 3, 4, 5]
# cargar_lista_aleatoriamente(mi_lista)
# print(mi_lista)

#------------------------------------------------------------------------------

# como buscar un dato en una lista y extraer su indice.

# def buscar_dato_en_lista(dato:int, lista:list)-> int | bool:
#     retorno = None
#     coincidencias = []
#     for i in range(len(lista)):
#         if dato == lista[i]:
#             coincidencias += [i]
#     return coincidencias


# lista = [5, 3, 7, 2, 10, 7]
# print(buscar_dato_en_lista(7, lista))

#------------------------------------------------------------------------------

# Listas paralelas
# lista_nombres = ["Juan", "Alberto", "Carlos", "Pepe", "Agustin"]
# lista_edades = [23, 12, 30, 10, 18]

# Para que existan las listas paralelas, debe haber 2 listas de
# igual cantidad de indices; que por medio de ellos se relacionan.

# for i in range(len(lista_nombres)):
#     if lista_edades[i] >= 18:
#         print(f"{lista_nombres[i]} es mayor de edad")
#     else:
#         print(f"{lista_nombres[i]} es menor de edad")