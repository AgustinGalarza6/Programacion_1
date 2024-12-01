# Python- Ejercicios iniciales - Entradas y Salidas

'''
#Ejercicio 1
Escribir un programa que muestre por pantalla “bienvenidos a la utn”
print("bienvenidos a la utn")
'''

'''
# Ejercicio 2
#Escribir un programa que pregunte el nombre del usuario en la consola(usando input) y
#después de que el usuario lo introduzca muestre por pantalla la cadena ”<nombre>”,
#donde <nombre> es el nombre que el usuario haya introducido.

print("Bienvenido al sistema.")
print("A continuación ingrese su nombre de usuario")

while True:
    nombre = input("\nIngrese su nombre de usuario: ")
    
    if nombre == "":
        print("Error: No ha ingresado su nombre.")
    else:
        break  # Salir del bucle si el nombre es válido

print(f"Su nombre es: {nombre}")

'''

'''
# Ejercicio 3

Se deberá obtener tanto el nombre como la edad usando input y luego mostrar los datos
concatenados con print.

Ej: "Usted se llama José y su edad es 66 años"

print("Bienvenido")
print("\tPor favor ingrese los siguientes datos: ")
nombre = (input("\tCual es su nombre?: "))
edad = (input("\tY cual es su edad?: "))

print(f"\tTu nombre es {nombre}, y tenes {edad} años.")


'''
'''
Ejercicio 4
Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y
operador_b), transformarlos en números enteros, realizar la operación suma y luego mostrar
el resultado de la misma utilizando print.
Ej: "El resultado de la suma es: 755

operador_A = int(input("Ingresa el primer operando: "))
operador_B = int(input("Ingresa el segundo operando: "))

suma = operador_A + operador_B

print(f"El resultado de la suma es: {suma}")
'''

'''
Ejercicio 5
Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y
división), tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y
operador_b), transformarlos en números enteros, realizar dicha operación y luego mostrar el
resultado de la misma utilizando print.
Ej: "El resultado de la …… es: 755"

operador_A = int(input("Ingresa el primer operador: "))
operador_B = int(input("Ingresa el segundo operador: "))

suma = operador_A + operador_B
resta = operador_A - operador_B
multiplicacion = operador_A * operador_B
division = operador_A / operador_B

print(f"El resultado de la suma es: {suma}.")
print(f"El resultado de la resta es: {resta}.")
print(f"El resultado de la multiplicacion es: {multiplicacion}.")
print(f"El resultado de la division es: {division}.")
'''

'''
Ejercicio 6
Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y
operador_b), transformarlos en números enteros, realizar la operación que nos permita
obtener el resto de una división y luego mostrar el resultado de la misma utilizando print.
Ej: "El resto de dividir 7 por 2 es: 1"

operador_A = int(input("Ingresa el primer operando: "))
operador_B = int(input("Ingresa el segundo operando: "))

resto = operador_A % operador_B

print(f"El resto de la division es: {resto}.")
'''

'''
Ejercicio 7
Tenemos que obtener el sueldo (por input) que el usuario nos ingrese , transformarlo en
número entero y mostrar el importe de sueldo actualizado con el incremento del 15%
utilizando print.

print("Bienvenido a la calculadora de sueldos.")
sueldo = int(input("Ingrese su sueldo: "))
sueldo_incrementado = sueldo * 0.15

print(f"Su nuevo sueldo con el incremento de un %15 es: {sueldo + sueldo_incrementado}.")
print(f"Su aumento fue de: {sueldo_incrementado}.")
'''

'''
Ejercicio 8
Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),
transformarlos en números enteros y mostrar el importe de sueldo actualizado con el
incremento porcentual utilizando print.

while True: 
    try:
        sueldo = input("Ingrese su sueldo: ")
        sueldo = int(sueldo)

        incremento = input("Ingrese el porcentaje de incremento: ")
        incremento = int(incremento)

        sueldo_incrementado = sueldo + (sueldo * incremento / 100)

        print(f"Su nuevo sueldo con el incremento de un {incremento}% es: {sueldo_incrementado}.")
        
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")
'''
        
'''
Ejercicio 9
Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por
consola(input), transformar en número y mostrar el importe actualizado con un descuento
del 20% utilizando print.

while True:
    try:
        importe = (input("Ingrese el importe o [pulse '0' para salir]: "))
        importe = int(importe)
        
        if importe == 0:
            print("Nos vemos maquinola!!")
            break

        descuento = importe * 0.20
        print(f"Su importe final con el descuento del %20 es de: {importe - descuento}")
    except:
        print("Error: Por favor, ingrese un valor numérico.")
        
'''

'''
Ejercicio 10
Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el
usuario por consola, transformarlos en números y mostrar el importe actualizado con el
descuento utilizando print.

importe = int(input("Ingrese el importe: "))
descuento = int(input("Ingrese el descuento: "))

print(f"El importe con el descuento del {descuento}% es: {importe - (importe * descuento / 100)}.")
'''

'''
Ejercicio 11
Agencia de viaje:
Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por
kilo de pasajero es 1000 pesos.Se ingresan todos los datos por PROMPT los datos a solicitar
de dos personas son: nombre, edad y peso
Se pide armar el siguiente mensaje:
"Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos ,
el promedio de edad es 33 y su viaje vale 140000 pesos "

#Datos persona 1
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = int(input("Ingrese su peso: "))

#Datos persona 2
nombre_2 = input("Ingrese el nombre del acomñante: ")
edad_2 = int(input("Ingrese la edad del acomñante: "))
peso_2 = int(input("Ingrese el peso del acomñante: ")) 

print(f"Hola {nombre} y {nombre_2}, sus pesos son de {peso} kilos y {peso_2} kilos respectivamente, sumados ambos es un total de {peso + peso_2} kilos, el promedio de sus edades es de{edad + edad_2} y su viaje vale {peso * 1000 + peso_2 * 1000}.")
'''


'''Empresa de Camiones:
Para el departamento de logística:

A. Es necesario saber la cantidad de camiones que harían falta para transportar los
materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la
cantidad de toneladas necesarias de materiales a transportar. El programa deberá
informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por
viaje 3500kg.

B. A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones
para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo
(en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir
a una velocidad máxima y constante de 90 km/h.

# PUNTO A
validacion = "s"

while True: 
    if validacion == "s" or validacion == "S":
        print("Bienvenido a la empresa de camiones")
        print("A continuacion informenos cuantas toneladas necesita transportar:")

        total_toneladas_necesarias = int(input("\n\t[+] Ingrese la cantidad total de toneladas que se debe transportar: "))

        #Conversion de unidad de toneladas a kilos para un calculo mas limpio
        total_toneladas_necesarias = total_toneladas_necesarias * 1000

        # Teniendo en cuenta que cada camion transporta 3500kg por viaje aplicamos la siguiente formula 
        camiones = total_toneladas_necesarias // 3500 # 

        print(f"\n\t[-] Para transportar {total_toneladas_necesarias} kg, se necesitan {camiones} camiones.")

        # PUNTO B

        kilometros_a_recorrer = int(input("\n\n\t[+] Ahora informenos cuantos kilometros necesita recorrer cada camion: "))

        horas_de_viaje = kilometros_a_recorrer // 90

        print(f"\n\t[-] Para recorrer {kilometros_a_recorrer} km, cada camion tarda {horas_de_viaje} horas.")
    
    if validacion != "s" or validacion != "S":
        validacion = input("\nDesea realizar otro calculo? [S] Si - [CUALQUIER TECLA] No: ")
        print("Gracias por elegirnos. ¡Hasta pronto!")
        break
'''

