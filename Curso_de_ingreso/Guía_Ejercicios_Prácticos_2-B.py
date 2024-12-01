#Crear un programa que pueda sumar los números pares comprendidos
#entre el 1 y el 10

contador_numeros_pares = 0

for i in range(1, 11):
    if i % 2 == 0:
        contador_numeros_pares += 1

print("El número de números pares entre 1 y 10 es:", contador_numeros_pares)


#Crear un programa que solicite al usuario que ingrese una contraseña
#mediante prompt.
#Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no
#coincidir, volver a solicitarla hasta que coincidan.

print("Bienvenido al sistema")

contraseña_correcta = "utn750"
password_usuario = input("Ingrese su contraseña: ")

while password_usuario != contraseña_correcta:
    print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
    password_usuario = input("Ingrese su contraseña nuevamente: ")

print("¡Contraseña correcta! Bienvenido.")



#Crear un programa que solicite al usuario que ingrese un número.
#Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
#coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.

numero_ingresado = int(input("Ingresa un número entre 0 y 9: "))

while (numero_ingresado < 0) or (numero_ingresado > 9):
    print("El número no se encuentra entre 0 y 9. Por favor, inténtelo de nuevo.")
    numero_ingresado = int(input("Ingresa un número entre 0 y 9: "))
    
print ("El numero ingresado se encuentra entre 0 y 9. Su numero fue:",numero_ingresado)

    
#Crear un programa que solicite al usuario que ingrese una letra. Se deberá
#validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).

#En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
#la condición se cumpla

letra_ingresada = input("Ingresa una letra en Mayuscula: ")

while letra_ingresada not in ["U", "T", "N"]:
    print("La letra no coincide con U, T o N. Por favor, inténtelo de nuevo.")
    letra_ingresada = input("Ingresa otra letra en Mayuscula: ")
    
print ("La letra ingresada coincide con U, T o N. Su letra fue:",letra_ingresada)



#Crear un programa que solicite 5 números mediante prompt. Calcular la
#suma acumulada y el promedio de los números ingresados.

suma = 0
contador = 0

# Solicitamos 5 números
while contador < 5:
    numero = int(input("Ingresa un número: "))
    suma += numero
    contador += 1

promedio = suma / 5

print("La suma acumulada es:", suma)
print("El promedio es:", promedio)
