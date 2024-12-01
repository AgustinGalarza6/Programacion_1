'''
#Realizar un programa que muestre por terminal el mensaje: “Esto no anda: funciona”.
print('Esto no anda: funciona')


Realizar un programa que pida el ingreso del nombre de una persona por input y lo muestre con el formato: “Su nombre es: ___“

nombre = input('Dame un nombre: ')
#msj = 'Su nombre es: ' + nombre
#print(msj)
#print('Su nombre es:', nombre)

print(f'Su nombre es: {nombre}')


Realizar un programa que pida el ingreso del nombre y la edad de una persona por input. Mostrar la información con el siguiente formato: “Su nombre es: ____ y tiene: ___ años”

nombre = input('Dame un nombre: ')
edad = input('Dame una edad: ')

print(f'Su nombre es: {nombre} y tiene: {edad} años')


Realizar un programa que permita el ingreso de dos números. Realizar la suma de los mismos y mostrar el resultado por pantalla con el siguiente formato: “La suma de los dos números es: ___”
# str = string - cadena de texto
# int = integer - entero
# float = floating - flotante 

num1 = input('Dame el numero 1: ')
num2 = input('Dame el numero 2: ')
#valido

num1 = int(num1)
num2 = int(num2)
print(f'La suma de los dos números es: {num1 + num2}')


Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).

num1 = int(input('Dame el numero 1: '))
num2 = int(input('Dame el numero 2: '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

msj = '\n\n'
msj += '[CALCULADORA]\n\n'
msj += '\t[+] Suma: ' + str(suma) + '\n'
msj += '\t[-] Resta: ' + str(resta) + '\n'
msj += '\t[*] Multiplicacion: ' + str(multiplicacion) + '\n'
msj += '\t[/] Division: ' + str(division)

print(msj)


Realizar un programa que pida dos números enteros. Calcular y mostrar el resto de la división entre ambos números. Ej: "El resto de dividir 7 por 2 es: 1" .

num1 = int(input('Dame el numero 1: '))
num2 = int(input('Dame el numero 2: '))

resto = num1 % num2
print(resto)


1) Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.

2) Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.

3)Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.

==
!=
>
<
>=
<=

edad = int(input('Dame una edad: '))

if edad > 25:
    print('mensaje 1')
else: 
    # ACA TENGO TODO EL UNIVERSO MENOR A 25
    if edad > 12 and edad < 20:
        if edad == 18:
            print('regalo 2')
        print('regalo')
        
'''

#Condicionales: Ferrete Lámparas.
#En una ferretería se desea implementar un sistema que permita a los clientes conocer cuánto deben pagar por la compra de lámparas de bajo consumo. Cada lámpara tiene un costo fijo de $800. El sistema debe aplicar los siguientes descuentos:


flag_descuento_adicional= False
coste_total = 0
coste_final = 0
descuento = 0
descuento_adicional = 0
porcentaje_descuento = 0
cantidad_de_lamparas = 0
costo_lampara = 800
marca_argentina_luz = "Argentina Luz"
marca_felipe_lamparas = "Felipe Lamparas"
marca_otros = "Otros"

menu = "SELECCIONE LA MARCA A COMPRAR\n\n[1] Argentina Luz\n[2] Felipe Lamparas\n[3] Otra marca\n\n[0] SALIR\n\n\tOPCION: "

marca = input(menu)
#Validacion
while marca != "1" and marca != "2" and marca != "3" and marca != "0":
    print("[ERROR] MARCA NO VALIDA")
    marca = input(menu)
#

if marca != "0":
    # MAPPEO LA OPCION CON EL LITERAL DE LA MARCA
    if marca == "1":
        marca = marca_argentina_luz
    else:
        if marca == "2":
            marca = marca_felipe_lamparas
        else:
            marca = marca_otros

    # PIDO CANTIDAD DE LAMPARAS A COMPRAR
    cantidad_de_lamparas = int(input("[+] INGRESE LA CANTIDAD DE LAMPARAS A COMPRAR: "))
    while cantidad_de_lamparas < 1:
        cantidad_de_lamparas = int(input("[ERROR] INGRESE LA CANTIDAD DE LAMPARAS A COMPRAR: "))

    # ACA EMPIEZA LA LOGICA DE DESCUENTOS
    if cantidad_de_lamparas >= 6:
        porcentaje_descuento = 0.5
    elif cantidad_de_lamparas == 5:
        if marca == marca_argentina_luz:
            porcentaje_descuento = 0.4
        else:
            porcentaje_descuento = 0.3
    elif cantidad_de_lamparas == 4:
        if marca == marca_argentina_luz or marca == marca_felipe_lamparas:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.2
    elif cantidad_de_lamparas == 3:
            if marca == marca_argentina_luz:
                porcentaje_descuento = 0.15
            elif marca == marca_felipe_lamparas:
                porcentaje_descuento = 0.1
            else:
                porcentaje_descuento = 0.05

    # CALCULO DE DESCUENTO POR CANTIDAD DE LAMPARAS Y MARCA
    coste_total = cantidad_de_lamparas * costo_lampara
    descuento = coste_total * porcentaje_descuento
    coste_final = coste_total - descuento

    # CALCULO DE DESCUENTO ADICIONAL 
    if coste_final > 4000:
        descuento_adicional = coste_final * 0.05
        coste_final -= descuento_adicional # coste_final = coste_final - descuento_adicional
        flag_descuento_adicional = True

    # INFORMES
    print(f"La marca elegida es: {marca}")
    print(f"La cantidad de lamparas compradas: {cantidad_de_lamparas}")    
    print(f"Coste total a pagar sin descuento: {coste_total}")  

    if porcentaje_descuento != 0:
        print(f"Descuento aplicado: {descuento}")  

    if descuento_adicional == True:
        print(f"Descuento adicional aplicado: {descuento_adicional}") 

    print(f"Total a pagar con descuentos aplicados: {coste_final}")

else:
    print("Gracias por elegirnos. ¡Hasta pronto!")