# Conversion de C a F
print("Bienvenido!")
grados_celcius = float(input("Ingrese la temperatura en grados celcius: "))
# Conversion a Grados Fahrenheit
grados_fahrenheit = (grados_celcius * 1.8) + 32
print("La temperatura en grados Fahrenheit es:", grados_fahrenheit)


# Calcular factorial de un numero
numero = int(input("Ingrese un numero: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de", numero, "es:", factorial)