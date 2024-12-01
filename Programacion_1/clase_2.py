# el acoplamientop es la dependencia que tienen las funciones entre si
# cuanto mas independientes sean mejor

# indepencia: autonomia de las funciones (una funcion no debe depender de otra)

# A la hora de crear funciones: Ingresar el nombre en snacke case y un verbo.

# Las variables locales nacen y mueren dentro de una funcion

# Ls funciones se ejecutan siempre de manera secuencial.

# Ejemplo:

def sumar():
    num_a = 10
    num_b = 20
    resultado = num_a + num_b
    return resultado

print(sumar())

# En este caso (a, b) seria un ejemplo grafico de variables locales.
def restar (a, b):
    return a - b

print(restar(10, 5))

# Los parametros se asignan por posicion o nombres
# En esta cursada vamos a trabajarlos mas por posiciones.

def agregar_iva(producto, iva=1.21): # PARAMETROS FORMALES
    resultado = producto * iva
    return resultado

suma = int(input("Ingresa un numero: "))
resultado = agregar_iva(suma)
print("El resultado del iva es: ", resultado)

print("============================================")
# los parametros opcionales van despues de los obligatorios (paramnetro obligatorio(producto), iva = 1.21 (opcional))

resultado = agregar_iva(suma, 1.105) # PARAMETROS ACTUALES
print("El resultado del iva es: ", resultado)

# PARAMETROS FORMALES: SON AQUELLAS VARIABLES DEFINIDAS EN LA FUNCION.
# PARAMETROS ACTUALES: SON AQUELLAS VARIABLES QUE RECIBE LA FUNCION.

# Definicion de tipos de datos en funciones
# def agregar_iva (monto:int, iva=float=1.21) -> float

# Las variables locales nacen y mueren dentro de una funcion
# Existen unicamente dentro de la funcion

# Tambien existen las variables globales (PROHIBIDO)
# Que es una variable global?


# ejemplo
'''
mi_variable = 10
print(mi_variable)

def agregar_iva (monto:int, iva:float=1.21) -> float:
    # GLOBAL UNIFICA LOS PARAMETROS ACTUALES Y FORMALES.
    global mi_variable
    mi_variable = 20
    resultado = monto * iva
    return resultado

agregar_iva(1000)
print(mi_variable)
'''

# La referencia es donde se aloja el valor tipo de dato y el id.

# REF por valor significa que la variable recibe el dato por valor
# ej: numero = 10 (trabaja con el valor "10" no se maneja por referencia y no puede ser modificado)

# REF por referencia significa que la variable recibe el dato por referencia
# ej: numero = 10 (esta puede ser modificada, accediendo a la referencia en memoria)

# En PYTHON los parametros de una funcion se trabaja por referencia

# Tipos de datos INMUTABLES:
# int, float, str, bool, tuple

# Tipos de datos MUTABLES:
# list, dict, set

numero = 5
print(id(numero), numero)
numero = 7
print(id(numero), numero)

# Como estos datos son inmutables, no se pueden cambiar. Se destruye el 5 y posteriormente se
# crea el 7 y se le asigna un nuevo espacio en celda o id.

lista = [1, 2, 3]
print(id(lista), lista)
# Modificamos la lista por que es mutable
lista += [4, 5, 6]
print(id(lista), lista)

def testear_inmutabilidad(numero:int):
    # numero = numero + 5
    numero += 5
    print("El numero fue modificado", numero)

def testear_inmutabilidad2(lista:list):
    lista += [5]
    print("La lista fue modificada", lista)

numero_ingresado = int(input("Ingresa un numero: "))
print(numero_ingresado)
testear_inmutabilidad(numero_ingresado)
print(numero_ingresado)

lista_principal = [1, 2, 3]
print(lista_principal)
testear_inmutabilidad2(lista_principal)
print("La lista final modificada es: ",lista_principal)

lista_a = [1, 2, 3]
lista_b = lista_a # CON ESTO APUNTAMOS LA LISTA B A LA MISMA CELDA DE MEMORIA DE LISTA A. Quedando ambas iguales sumandole la modificacion
# porque en pocas palabras apunta al mismo objeto en memoria.
lista_b += [4, 5, 6]
print("La lista a es: ",lista_a)
print("La lista b es: ",lista_b)

# Las funciones para estar completas tienen que tener "Documentacion"

def validar_entero(min:int, max:int, mensaje:str) -> str:
    '''
    Esta funcion solicita un dato del usuario y lo valida
    Recibe: min del tipo int (es el rango minimo de validacion)
            max (es el rango maximo de validacion)
            mensaje (es el texto que se muestra al usuario para que ingrese los datos)
    Devuelve un numero entero validado.

    '''
    numero_entero = int(input(mensaje))
    while numero_entero < min or numero_entero > max:
        numero_entero = int(input(mensaje))
    return numero_entero

anio = validar_entero(1900, 2024, "Ingresa un anio: ")
nota = validar_entero(0, 10, "Ingresa una nota: ")