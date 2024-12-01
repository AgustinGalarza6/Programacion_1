#PRUEBAS

contador = 0
edad_jugador_mas_joven = None
nombre_jugador_mas_joven = None

while contador < 3:
    # CAPTURAMOS EL NOMBRE DEL JUGADOR
    nombre_del_jugador = input("Nombre del jugador: ")
    while not nombre_del_jugador.isalpha():
        print("Nombre no válido.")
        nombre_del_jugador = input("Ingrese de nuevo el nombre: ")
            
    # CAPTURAMOS LA EDAD DEL JUGADOR
    edad_del_jugador = input("¿Qué edad tiene? (no menor a 18): ")
    while not edad_del_jugador.isdigit() or int(edad_del_jugador) < 18:
        print("Edad no válida.")
        edad_del_jugador = input("Ingrese de nuevo la edad: ")
    edad_del_jugador = int(edad_del_jugador)  # Convertimos la edad a entero después de la validación
    
    # Comparación para encontrar el jugador más joven
    if edad_jugador_mas_joven == None or edad_del_jugador < edad_jugador_mas_joven:
        edad_jugador_mas_joven = edad_del_jugador
        nombre_jugador_mas_joven = nombre_del_jugador
    
    contador += 1

# INFORME
if nombre_jugador_mas_joven != None:
    print(f"El jugador más joven es {nombre_jugador_mas_joven} con {edad_jugador_mas_joven} años.")
else:
    print("No se ingresaron jugadores válidos.")