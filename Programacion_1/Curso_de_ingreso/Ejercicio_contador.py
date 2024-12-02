# Solicitar al usuario que ingrese el número inicial del contador y cuante hasta otro ingresado.
desde = int(input("Ingresa el número desde el cual contar: "))
hasta = int(input("Ingresa el número hasta el cual contar: "))

for numeros in range(desde, hasta + 1):
        print(numeros)