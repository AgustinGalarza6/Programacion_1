# Tu tarea es crear el código teniendo en cuenta los siguientes puntos:

# pedirá al usuario que ingrese un número entero;

# Utilizará un bucle while;

# Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! 
# ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla,
# y el mago debe decir las siguientes palabras: "¡Bien hecho, Junior! Eres libre ahora."

print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior! Introduce un número entero |
| y adivina qué número he elegido para ti. |
| ¿Cuál es el número secreto? |
+================================+
""")

numero_del_usuario = int(input("Ingresa un numero: "))

numero_del_mago = 8

while (numero_del_mago != numero_del_usuario):
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero_del_usuario = int(input("Ingresa otro: "))
else:
    print("¡Bien hecho, Junior! Eres libre ahora.")