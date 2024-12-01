'''
Alta: Desarrolle una función que permita cargar un diccionario a partir de los datos que ingresa el
usuario por consola, los datos se componen por un nombre de alumno y 2 calificaciones (primer y
segundo examen parcial).
'''
def menu():
    menu = '''
1) Cargar datos
2) Mostrar datos
3) Calcular promedio
4) Informar estado académico
5) Buscar alumno
6) Baja física
7) Baja Logica
0) Salir del programa

Ingrese una opcion: 
'''
    respuesta = "n"
    lista_de_alumnos = []

    while respuesta == "n":
        seleccionar_opcion = input(menu)

        match seleccionar_opcion:
            case "1":
                alumno = cargar_datos("nombre", "nota_1", "nota_2", "activo")
                lista_de_alumnos.append(alumno)
            case "2":
                mostrar_lista_alumnos(lista_de_alumnos)
            case "3":
                calcular_promedio(lista_de_alumnos, "promedio")
                mostrar_lista_alumnos(lista_de_alumnos)
            case "4":
                informar_estado_academico(lista_de_alumnos, "promedio")
            case "5":
                alumno_a_buscar = input("ingrese el nombre del alumno que busca: ")
                resultado_busqueda = buscar_alumno(lista_de_alumnos, alumno_a_buscar)
                if resultado_busqueda == None:
                    print(f"no se encontro el alumno de nombre {alumno_a_buscar}") 
                else:
                    mostrar_titulo(lista_de_alumnos)
                    mostrar_un_alumno(resultado_busqueda)
            case "6":
                alumno_a_eliminar = input("Ingrese el alumno a eliminar: ")
                borrar_alumno(lista_de_alumnos, alumno_a_eliminar)
            case "7":
                alumno_a_dar_de_baja = input("Ingrese el nombre a dar de baja: ")
                diccionario_a_dar_de_baja = buscar_alumno(lista_de_alumnos , alumno_a_dar_de_baja)
                if diccionario_a_dar_de_baja == None:
                    print(f"no se encontro el alumno de nombre {alumno_a_buscar}") 
                else:
                    diccionario_a_dar_de_baja.update({"activo":False})
                    print("Se desactivo al alumno", diccionario_a_dar_de_baja["nombre"])
            case "8": 
                pass
            case "9":
                pass
            case "10":
                pass
            case "0":
                print("Cerrando programa")
                break
            case _:
                print("Opcion no valida, ingres un numero del 1 al 10")



def validar_rango(numero: str, minimo: int, maximo: int)-> bool:
    '''
    
    '''
    numero_valido = False

    if numero.isdigit() == True:
        if int(numero) >= minimo and int(numero) <= maximo:
            numero_valido = True

    return numero_valido
    
def cargar_datos(clave_nombre: str, calificacion_1:str, calificacion_2:str, clave_estado:str) -> dict:
    '''
    
    '''
    nombre_ingresado = input(f"Ingrese el {clave_nombre} del alumno: ")
    
    califiacion_1_ingresada = input(f"Ingrese la {calificacion_1} del alumno: ")
    while validar_rango(califiacion_1_ingresada, 1, 10) == False:
        califiacion_1_ingresada = input(f"Ingrese la {calificacion_1} del alumno: ")
    califiacion_1_ingresada = int(califiacion_1_ingresada)

    califiacion_2_ingresada = input(f"Ingrese la {calificacion_2} del alumno: ")
    while validar_rango(califiacion_2_ingresada, 1, 10) == False:
        califiacion_2_ingresada = input(f"Ingrese la {calificacion_2} del alumno: ")
    califiacion_2_ingresada = int(califiacion_2_ingresada)

    alumno = {clave_nombre: nombre_ingresado, calificacion_1: califiacion_1_ingresada, calificacion_2: califiacion_2_ingresada, clave_estado: True }

    return alumno


# 2) Desarrolle una función que muestre una lista de alumnos y sus respectivos datos en filas y columnas,
# donde cada fila representa un alumno y cada columna representa uno de sus datos.

def mostrar_un_alumno(alumno: dict) -> None:
    """
    """
    for clave in alumno.keys():
        if clave != "activo" :
            
            print(f"{alumno[clave]:>10}", end="")

def mostrar_titulo(lista_alumnos: list[dict]) -> None:
    """
    """

    if len(lista_alumnos) > 0:
        lista_claves = lista_alumnos[0].keys()
        for clave in lista_claves:
            if clave != "activo":
                print(f"{clave.upper():>10}", end="")
        print()
    else:
        print("Lista vacía")

def mostrar_lista_alumnos(lista_alumnos: list) -> None:
    """
    """
    # print("Nombre Nota1 Nota2")
    mostrar_titulo(lista_alumnos)
    for i in range(len(lista_alumnos)):
        un_alumno = lista_alumnos[i]
        # print(un_alumno["nombre"], un_alumno["nota_1"], un_alumno["nota_2"])
        if un_alumno["activo"] == True:
            mostrar_un_alumno(un_alumno)
            print(" ")

# 3) Modificación: Desarrolle una función que permita calcular el promedio de calificaciones a partir de
# una lista de alumnos. Recibe una lista de diccionarios por parámetro, calcula el promedio y lo agrega
# como un ítem más al diccionario.

def calcular_promedio(lista_alumnos:list, clave:str) -> None:
    """_summary_

    Args:
        diccionario (dict): _description_
    """
    for i in range(len(lista_alumnos)):
        # promedio = (lista_alumnos[i]["nota_1"] + lista_alumnos[i]["nota_2"]) / 2        
        alumno = lista_alumnos[i]
        promedio = (alumno["nota_1"] + alumno["nota_2"]) / 2 
        alumno.update({clave:promedio})

# 4) Desarrolle una función que informe por cada alumno de la lista su estado académico (promedio de 1 al
# 4: desaprobado, 4 o 5: aprobado, y 6 o más: promocionado).

def informar_estado_academico(lista_alumnos:list, clave:str)->None:
    """
    """
    for alumno in lista_alumnos:
        if clave in alumno.keys():
            if alumno[clave] < 4:
                print(f"El alumno {alumno['nombre']} está desaprobado")
            elif alumno[clave] < 6:
                print(f"El alumno {alumno['nombre']} está aprobado")
            else:
                print(f"El alumno {alumno['nombre']} promociono la materia")
        else:
            print(f"[ERROR] el alumno: {alumno['nombre']} no tiene promedio calculado")


# 5) Desarrolle una función que informe las notas y el promedio del alumno cuyo nombre recibe por
# parámetro, en caso de no encontrarlo deberá imprimir un mensaje de error.


def buscar_alumno(lista_alumnos: list, nombre: str) -> dict|None:
    """
    """
    retorno = None
    for alumno in lista_alumnos:
        if alumno["nombre"] == nombre:
            retorno = alumno
            break
    return retorno

# 6) Baja Física: Desarrolle una función que pueda eliminar a un alumno de la lista de alumnos. El alumno
# a eliminar deberá seleccionarlo el usuario por terminal, validar que exista antes de eliminarlo, y en
# caso de que no exista mostrar un mensaje de error.

def borrar_alumno(lista_alumnos: list, nombre: str)->None:
    """
    """
    alumno_buscado = buscar_alumno(lista_alumnos, nombre)
    if  alumno_buscado == None:
        print(f"El alumno no se encuentra en la lista")
    else:
        print(f"Se elimino al alumno {alumno_buscado['nombre']}")
        lista_alumnos.remove(alumno_buscado)


# 7) Baja Lógica: Desarrolle una función que pueda dar de baja lógicamente a un alumno de la lista.
# Deberá recibir por parámetro el nombre del alumno a eliminar y agregarle un estado (bool) activo o
# inactivo. Modificar la función que muestra los alumnos haciendo que ignore a todos los alumnos
# inactivos.





# ----------------------------------------------------------------------




menu() 
