# Ejercicio 1
nombre_de_usuario = input("Ingresa tu nombre de usuario: ")
print("Bienvenido:",nombre_de_usuario)


# Ejericio 2
num_1 = int(input("Ingresa un numero: "))
num_2 = int(input("Ingresa otro numero: "))
print("La suma de estos numeros es:",num_1 + num_2)


# Ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")

print("Hola:", nombre, apellido, "tienes", edad, "años")


# Ejercicio 4
nombre_completo = input("Ingresa tu nombre completo: ")
numero_de_comision = input("Ingresa tu numero de comision: ")
asignatura = input("Ingresa tu asignatura: ")
docente = input("Ingresa tu docente: ")
presente = input("¿Estuvo presente el dia miercoles?: ")

print("Hola:", nombre_completo)
print("tu numero de comision es:", numero_de_comision)
print("tu asignatura es:", asignatura,)
print("tu docente es:", docente)
print("¿Estuvo presente el dia miercoles?:", presente)


# Ejercicio 5
primer_lado = int(input("Ingresa el primer lado del cuadrado: "))
segundo_lado = int(input("Ingresa el segundo lado del cuadrado: "))

print("La superficie del cuadrado es:", primer_lado * segundo_lado)


# Ejercicio 6
largo = int(input("Ingresa el largo del rectangulo: "))
ancho = int(input("Ingresa el ancho del rectangulo: "))

print("La superficie del rectangulo es:", largo * ancho)


# Ejercicio 7
base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

print("La superficie del triangulo es:", (base * altura) / 2)


# Ejericio 8
nombre_del_producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))

print("El precio final del producto + IVA es:", (precio * 1.21))


# Ejercicio 9
nombre_y_apellido = input("Ingresa tu nombre y apellido: ")
nota_1 = input("Ingresa tu primer nota: ")
nota_2 = input("Ingresa tu segunda nota: ")
nota_3 = input("Ingresa tu tercer nota: ")

nota_final = (float(nota_1) + float(nota_2) + float(nota_3)) / 3

print("El promedio final es:", nota_final)


# Ejercicio 10
nombre_de_usuario = input("Ingrese su nombre completo por favor: ")
edad_del_usuario = input("Ingrese su edad por favor: ")
edad_dentro_de_10_años = int(edad_del_usuario) + 10

print("Hola,", nombre_de_usuario, "dentro de 10 años tendras:", edad_dentro_de_10_años, "años.")