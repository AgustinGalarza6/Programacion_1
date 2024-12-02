from Biblioteca_funciones import *

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Notas:
# 1) El programa debe contener un archivo .py que incluya el menú principal y las llamadas a las funciones
# necesarias para completar el programa.
# 2) Las definiciones de todas las funciones deben estar en una biblioteca separada del programa principal.
# 3) Todas las funciones propias deben contar con la documentación correspondiente.
# 4) Pueden crear y utilizar tantas funciones principales y secundarias (auxiliares) como deseen, siempre
# respetando las buenas prácticas.
# 5) Cada opción del menú debe contemplar al menos una llamada de función (aunque no está limitada a
# una).
# 6) En caso de que el usuario ingrese un dato incorrecto, no se debe volver al menú. Se le pedirá que ingrese
# el dato nuevamente hasta que lo haga correctamente.
# 7) Está prohibido utilizar cualquier método de las clases string o list.
# 8) Todas las opciones del menú deben ser visibles en todo momento. Si no se puede acceder a alguna
# opción, se debe imprimir un mensaje informando al usuario la razón.
# Objetivos de Aprobación No Directa (Calificación de 4 a 5 puntos):
# - Opciones A, B, C, D, e I del menú funcionando completamente, respetando el enunciado.
# Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):
# - Opciones A, B, C, D, E, F, G, H, e I del menú funcionando completamente, respetando el enunciado.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Inicialización de banderas para validar la existencia de aspectos generados
# en puntos anteriores.

respuesta = "N"
numero_ingresado = None
lista_mayusculas = None
cantidad_filas = None
cantidad_columnas = None
matriz = None

menu = '''
    A) Ingresar un número entero entre 3 y 15.
    B) Generar lista de letras mayúsculas aleatorias.
    C) Mostrar lista de letras generadas.
    D) Buscar una letra mayúscula en la lista.
    E) Ordenar y mostrar copia de la lista (ASC o DESC).
    F) Ingresar dos números enteros (filas y columnas).
    G) Generar matriz de números aleatorios.
    H) Mostrar la matriz generada.
    I) Salir del programa.
    \nIngrese una opcion: 
'''
print("Bienvenido al programa. Por favor, elija una opcion del menu.")
print("-------------------------------------------------------------")
while respuesta == "N":
    opcion_seleccionada = input(menu)
    match opcion_seleccionada:
        case "A":
            numero_ingresado = solicitar_entero("Ingresa un numero entre 3 y 15: ")
            print("El numero ingresado fue:", numero_ingresado)
        case "B":
            if numero_ingresado == None:
                print('[ERROR] Debe generar la matriz en la "Punto A" antes de mostrarla.')
            else:
                print("Generando lista de letras mayusculas aleatorias...")
                lista_mayusculas = cargar_lista_con_mayusculas(numero_ingresado)
                print("Lista generada correctamente.")
        case "C":
            if lista_mayusculas == None:
                print('[ERROR] Debe generar la matriz en la "Punto B" antes de mostrarla.')
            else:
                print("Mostrando lista de letras generadas:")
                imprimir_lista(lista_mayusculas)
        case "D":
            if lista_mayusculas == None:
                print('[ERROR] Debe generar la matriz en la "Punto B" antes de mostrarla.')
            else:
                print("Buscar una letra mayuscula en la lista")
                letra_ingresada = solicitar_letra_mayuscula("Ingresa una letra mayuscula: ")
                resultado_busqueda = buscar_letra_en_lista(lista_mayusculas, letra_ingresada)
                print(resultado_busqueda)
        case "E":
            if lista_mayusculas == None:
                print('[ERROR] Debe generar la matriz en la "Punto B" antes de mostrarla.')
            else:
                criterio = solicitar_ordenamiento("Ingresa 'ASC' o 'DESC': ")
                lista_ordenada = ordenar_lista(lista_mayusculas, criterio)
                print("Lista ordenada:", lista_ordenada)
        case "F":
            print("Ingresar dos números enteros (filas y columnas):")
            numeros = solicitar_numeros(2, "Ingresa un numero entre 3 y 10: ")
            cantidad_filas, cantidad_columnas = numeros
            print(f"Se solicitaron {cantidad_filas} filas y {cantidad_columnas} columnas.")
        case "G":
            if (cantidad_filas == None) or (cantidad_columnas == None):
                print('[ERROR] Debe generar la matriz en la "Punto F" antes de mostrarla.')
            else:
                print("Generando matriz de numeros aleatorios...")
                matriz = crear_matriz(cantidad_filas, cantidad_columnas, 1)
                llenar_matriz_random(matriz, 1, 9)
                print("Matriz generada correctamente.")
        case "H":
            if matriz == None:
                print('[ERROR] Debe generar la matriz en la "Punto G" antes de mostrarla.')
            else:
                print("Mostrando la matriz generada:")
                mostrar_matriz_separada(matriz)
        case "I":
            respuesta = input("¿Desea salir del programa? S/N: ")
            if respuesta == "S":
                print("Saliendo del programa...")
            else:
                respuesta = "N"
        case _:
            print("Opcion incorrecta. Por favor, elija una opcion del menu.")