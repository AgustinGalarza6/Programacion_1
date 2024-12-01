#Practicas para el parcial, Miercoles 24/07/2024

#PUNTO 1

#En una partida de todos contra todos de CS-GO (Juego de disparos) un grupo de 5 amigos quiere saber las estadísticas al finalizar la partida.
#Para esto se requieren los siguientes datos:

#Nombre del jugador.

#Edad del jugador - Mayor de edad.

#Bajas (Cantidad de veces que mató) - Número positivo inclusive 0.

#Muertes (Cantidad de veces que murió) - Número positivo inclusive 0.

#INFORMAR
#A) Nombre del jugador más joven.
#B) El jugador que más bajas tuvo.
#C) El jugador que menos muertes tuvo.
#D) El promedio de bajas.
#E) Cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas están entre 10 y 15.
#F) El nombre y edad del jugador que más muertes tuvo.


# Inicialización de variables
nombre_jugador_mas_joven = ""
edad_jugador_mas_joven = None 
nombre_jugador_mas_bajas = None
mayor_bajas = 0
nombre_jugador_menos_muertes = ""
menor_muertes = None
bajas_totales = 0
jugadores_20_30_con_bajas_10_15 = 0
nombre_jugador_mas_muertes = None
mayor_muertes = 0
contador_ingresos = 0

validacion = "s"

while validacion == "s" or "S":
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
    edad_del_jugador = int(edad_del_jugador)
    
    # Comparación para encontrar el jugador más joven
    if edad_jugador_mas_joven is None or edad_del_jugador < edad_jugador_mas_joven:
        edad_jugador_mas_joven = edad_del_jugador
        nombre_jugador_mas_joven = nombre_del_jugador
    
    # CAPTURAMOS LAS BAJAS DEL JUGADOR
    bajas_del_jugador = input("¿Cuántas bajas tuvo? (no negativo): ")
    while not bajas_del_jugador.isdigit() or int(bajas_del_jugador) < 0:
        print("Bajas no válidas.")
        bajas_del_jugador = input("Ingrese de nuevo las bajas: ")
    bajas_del_jugador = int(bajas_del_jugador)
    
    # Acumulador de bajas para el promedio total
    bajas_totales += bajas_del_jugador
    
    # Lógica para el jugador que más mató
    if nombre_jugador_mas_bajas is None or bajas_del_jugador > mayor_bajas:
        mayor_bajas = bajas_del_jugador
        nombre_jugador_mas_bajas = nombre_del_jugador
    
    # CAPTURAMOS LAS MUERTES DEL JUGADOR
    muertes_del_jugador = input("¿Cuántas muertes tuvo? (no negativo): ")
    while not muertes_del_jugador.isdigit() or int(muertes_del_jugador) < 0:
        print("Muertes no válidas.")
        muertes_del_jugador = input("Ingrese de nuevo las muertes: ")
    muertes_del_jugador = int(muertes_del_jugador)
    
    # Lógica para el jugador con más muertes
    if nombre_jugador_mas_muertes is None or muertes_del_jugador > mayor_muertes:
        mayor_muertes = muertes_del_jugador
        nombre_jugador_mas_muertes = nombre_del_jugador
    
    # Lógica para el jugador con menos muertes
    if menor_muertes is None or muertes_del_jugador < menor_muertes:
        menor_muertes = muertes_del_jugador
        nombre_jugador_menos_muertes = nombre_del_jugador
    
    # Contamos cuántos jugadores tienen entre 20 y 30 años con bajas entre 10 y 15
    if 20 <= edad_del_jugador <= 30 and 10 <= bajas_del_jugador <= 15:
        jugadores_20_30_con_bajas_10_15 += 1
    
    contador_ingresos += 1
    validacion = input("\nDesea continuar? [S] Sí - [CUALQUIER TECLA] No: ")
    if validacion.lower() != 's':
        print("Gracias por usar nuestro sistema. ¡Hasta luego!\n")
        break

# INFORMES
# Punto a
if edad_jugador_mas_joven is not None:
    print(f"El jugador más joven es {nombre_jugador_mas_joven} con {edad_jugador_mas_joven} años.")

# Punto b
if nombre_jugador_mas_bajas is not None:
    print(f"El jugador con más bajas es {nombre_jugador_mas_bajas} con {mayor_bajas} bajas.")

# Punto c
if nombre_jugador_menos_muertes is not None:
    print(f"El jugador con menos muertes es {nombre_jugador_menos_muertes} con {menor_muertes} muertes.")

# Punto d
if contador_ingresos > 0:
    promedio_bajas = bajas_totales / contador_ingresos
    print(f"El promedio de bajas es: {promedio_bajas:.2f}")

# Punto e
print(f"La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas están entre 10 y 15 es: {jugadores_20_30_con_bajas_10_15}")

# Punto f
if nombre_jugador_mas_muertes is not None:
    print(f"El jugador con más muertes es {nombre_jugador_mas_muertes} con {mayor_muertes} muertes.")