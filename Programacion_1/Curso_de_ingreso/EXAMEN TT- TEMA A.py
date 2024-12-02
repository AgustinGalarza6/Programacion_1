#Es la gala final de Gran Hermano y la producción nos pide un programa para contar los votos de los
#televidentes y saber así quién será el ganador del programa.
#Los participantes finalistas son: Emma, Furia y Bautista.

#Para poder participar de la votación, el televidente debe ingresar:
#● Nombre del votante
#● Edad del votante (debe ser mayor a 13)
#● Género del votante (masculino, femenino, otro)
#● El nombre del participante a quien le dará el voto positivo (Validar entre las 3 opciones)
#● Realizó el pago con mercado pago (si o no)

#Se necesita saber:
#1. El promedio de edad de las votantes de género femenino que realizaron el pago con mercado pago..
#2. El nombre del participante que ganó el reality (El que tiene más votos).
#3. Nombre del votante más joven qué votó a Bautista.
#4. Nombre de cada participante y porcentaje de los votos que recibió.
#5. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Furia o a Emma.

#VARIABLES
validacion = "s"
votacion_femenino = 0
acumulador_edad_femenino = 0
votos_positivos_emma = 0
votos_positivos_bautista = 0
votos_positivos_furia = 0
nombre_votante_mas_joven_bautista = None
votos_totales = 0
cantidad_de_votantes_entre_25_y_40 = 0
edad_votante_mas_joven_bautista = None
ganador = None

while validacion == "s" or "S":
    
    # Capturamos el nombre del votante
    nombre_del_votante = input("Ingrese su nombre: ")
    while not nombre_del_votante.isalpha():
        print("Nombre no valido")
        nombre_del_votante = input("Ingrese de nuevo el nombre: ")

    # Capturamos la edad
    edad_del_votante = input("Ingrese su edad: ")
    while not edad_del_votante.isdigit() or int(edad_del_votante) < 13:
        print("Edad no valida")
        edad_del_votante = input("Ingrese de nuevo la edad: ")
    edad_del_votante = int(edad_del_votante)

    # Capturamos el género del votante
    genero_del_votante = input("Genero: \n[1] Masculino\n[2] Femenino\n[3] Otro genero\nIngrese una opcion: ")
    while (genero_del_votante != "1") and (genero_del_votante != "2") and (genero_del_votante != "3"):
        print("Genero no valido")
        genero_del_votante = input("Genero: \n[1] Masculino\n[2] Femenino\n[3] Otro genero\nIngrese una opcion: ")
    
    if genero_del_votante == "1":
        genero_del_votante = "Masculino"
        #Si es masculino y entre 25 y 40, y voto a furia o a emma
        if (genero_del_votante == "Masculino") and (edad_del_votante >= 25) and (edad_del_votante <= 40):
            if (participante_del_voto_positivo == "Emma") or (participante_del_voto_positivo == "Furia"):
                cantidad_de_votantes_entre_25_y_40 += 1
    elif genero_del_votante == "2":
        genero_del_votante = "Femenino"
        votacion_femenino += 1
    else:
        genero_del_votante = "Otro genero"
        
    # Capturamos el nombre del participante a quien le dará el voto positivo
    participante_del_voto_positivo = input("Participante: \n[1] Emma\n[2] Furia\n[3] Bautista\nIngrese una opcion: ")
    while (participante_del_voto_positivo != "1") and (participante_del_voto_positivo != "2") and (participante_del_voto_positivo != "3"):
        print("Participante no valido")
        participante_del_voto_positivo = input("Participante: \n[1] Emma\n[2] Furia\n[3] Bautista\nIngrese una opcion: ")
    #VALIDAMOS
    if participante_del_voto_positivo == "1":
        participante_del_voto_positivo = "Emma"
        #Contamos votos positivos
        votos_positivos_emma += 1
    elif participante_del_voto_positivo == "2":
        participante_del_voto_positivo = "Furia"
        #Contamos votos positivos para furia
        votos_positivos_furia += 1
    else:   
        participante_del_voto_positivo = "Bautista"
        #Contamos votos positivos para bautista
        votos_positivos_bautista += 1
        #Guardamos el nombre del votante mas joven
        if (edad_votante_mas_joven_bautista == None) or (edad_del_votante < edad_votante_mas_joven_bautista):
            edad_votante_mas_joven_bautista = edad_del_votante
            nombre_votante_mas_joven_bautista = nombre_del_votante
            
    #Contamos el voto ingreso no importa a quien se le dio el voto       
    votos_totales += 1
        
    # ¿Realizó el pago con mercado pago? (si o no)
    pago_con_mp = input("¿Realizó el pago con mercado pago? \n[1] Si\n[2] No\nIngrese una opcion: ")
    while (pago_con_mp != "1") and (pago_con_mp != "2"):
        print("Respuesta no valida")
        pago_con_mp = input("¿Realizó el pago con mercado pago? [1] Si\n[2] No\nIngrese una opcion: ")
    #VALIDAMOS
    if pago_con_mp == "1":
        pago_con_mp = "Si"
        if genero_del_votante == "Femenino":
            acumulador_edad_femenino += edad_del_votante
    else:
        pago_con_mp = "No"
        
    validacion = input("\nDesea continuar? [S] Si - [CUALQUIER TECLA] No: ")
    if validacion != 's' and validacion != 'S':
        print("Gracias por su voto!.\n")
        break
    
#Se necesita saber:
#1. El promedio de edad de las votantes de género femenino que realizaron el pago con mercado pago.
if (votacion_femenino > 0) and (pago_con_mp == "Si"):
    promedio_edad_femenino = acumulador_edad_femenino / votacion_femenino
    print(f"Promedio de edad de las votantes femeninas que pagaron con Mercado Pago: {promedio_edad_femenino}")
else:
    print("No hubo mujeres que hayan pagado con mercado pago")

#2. El nombre del participante que ganó el reality (El que tiene más votos).
if votos_positivos_emma > votos_positivos_furia and votos_positivos_emma > votos_positivos_bautista:
    ganador = "Emma"
elif votos_positivos_furia > votos_positivos_emma and votos_positivos_furia > votos_positivos_bautista:
    ganador = "Furia"
else:
    ganador = "Bautista"
print(f"El participante que ganó el reality es {ganador}")

#3. Nombre del votante más joven qué votó a Bautista.
if nombre_votante_mas_joven_bautista != None:
    print(f"El votante más joven que votó a Bautista fue {nombre_votante_mas_joven_bautista}")
else:
    print("No se encontraron votantes para Bautista")

#4. Nombre de cada participante y porcentaje de los votos que recibió.
if votos_totales != 0:
    #Porcentaje de emma
    porcentaje_emma = votos_positivos_emma / votos_totales * 100
    print(f"Porcentaje de votos de Emma es de: {porcentaje_emma}%")
    #Porcentaje de furia
    porcentaje_furia = votos_positivos_furia / votos_totales * 100
    print(f"Porcentaje de votos de Furia es de: {porcentaje_furia}%")
    #Porcentaje de bautista
    porcentaje_bautista = votos_positivos_bautista / votos_totales * 100
    print(f"Porcentaje de votos de Bautista es de: {porcentaje_bautista}%")

#5. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Furia o a Emma.
if cantidad_de_votantes_entre_25_y_40 != 0:
    print(f"La cantidad de personas de genero masculino entre 25 y 40 años que votaron a Furia o a Emma es {cantidad_de_votantes_entre_25_y_40}")
else:
    print("No se encontraron votantes entre ese rango de edades")
