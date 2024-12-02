#Ejercicio 2 parcial practica

# Punto 2
#En una veterinaria se están realizando censos para evaluar los animales ingresados por día.
#Por este motivo, se le realizará una consulta a los primeros 10 ingresos.
#Se requieren los siguientes datos:

#Tamaño de la mascota (Chica, Mediana o Grande).
#Sexo de la mascota (Hembra o Macho).
#Tipo de mascota (Gato, Perro, Otro).
#Edad de la mascota. Validar.
#Está vacunado SI/NO (Se puede utilizar boolean si se desea).
#
#INFORMAR
#
#A) Cuál es la mascota más vieja entre los tamaños medianos o grandes.
#B) Cuál es el promedio de edad de las gatas.
#C) Cuál es el tipo de mascota menos vacunado.
#D) El porcentaje de gatos, perros y otros.


validacion = "s"
contador_de_ingresos = 0
tamaño_de_mascota_mas_vieja = None
edad_mas_vieja = None

while validacion == "s" or "S" or contador_de_ingresos < 10:
    # Tamaño de la mascota
    tamano_de_mascota = input("¿Cuál es el tamaño de la mascota? \n[1]Chica\n[2]Mediana\n[3]Grande\n\tElige una opcion: ")
    while tamano_de_mascota != "1" and tamano_de_mascota != "2" and tamano_de_mascota != "3":
        print("El tamano de la mascota no es valido.")
        tamano_de_mascota = input("¿Cuál es el tamaño de la mascota? [1]Chica [2]Mediana [3]Grande: ")
    tamano_de_mascota = int(tamano_de_mascota)
    if tamano_de_mascota == 1:
        tamano_de_mascota = "Chica"
    elif tamano_de_mascota == 2:
        tamano_de_mascota = "Mediana"
    elif tamano_de_mascota == 3:
        tamano_de_mascota = "Grande"
    
    # Sexo de la mascota
    sexo_de_mascota = input("\n¿Cuál es el sexo de la mascota?: \n[1]Hembra\n[2]Macho\n\tElige una opcion: ")
    while sexo_de_mascota != "1" and sexo_de_mascota != "2":
        print("El sexo de la mascota no es valido.")
        sexo_de_mascota = input("¿Cuál es el sexo de la mascota?: \n[1]Hembra\n[2]Macho\n\tElige una opcion: ")
    sexo_de_mascota = int(sexo_de_mascota)
    if sexo_de_mascota == 1:
        sexo_de_mascota = "Hembra"
    elif sexo_de_mascota == 2:
        sexo_de_mascota = "Macho"
        
    # Tipo de mascota
    tipo_de_mascota = input("\n¿Cuál es el tipo de mascota?: \n[1]Gato\n[2]Perro\n[3]Otro\n\tElige una opcion: ")
    while tipo_de_mascota != "1" and tipo_de_mascota != "2" and tipo_de_mascota != "3":
        print("El tipo de mascota no es valido.")
        tipo_de_mascota = input("¿Cuál es el tipo de mascota?: \n[1]Gato\n[2]Perro\n[3]Otro\n\tElige una opcion: ")
    tipo_de_mascota = int(tipo_de_mascota)
    if tipo_de_mascota == 1:
        tipo_de_mascota = "Gato"
    elif tipo_de_mascota == 2:
        tipo_de_mascota = "Perro"
    elif tipo_de_mascota == 3:
        tipo_de_mascota = "Otro"
        
    # Edad de la mascota
    edad_de_mascota = input("\n¿Cuál es la edad de la mascota?: ")
    while not edad_de_mascota.isdigit():
        print("La edad de la mascota no es valida.")
        edad_de_mascota = input("¿Cuál es la edad de la mascota?: ")
    edad_de_mascota = int(edad_de_mascota)
    
    # Si es la primera mascota que estamos evaluando
    if edad_mas_vieja == None:
        if tamano_de_mascota == "Mediana" or tamano_de_mascota == "Grande":
            edad_mas_vieja = edad_de_mascota
            tamano_de_mascota_mas_vieja = tamano_de_mascota
    else:
        if tamano_de_mascota == "Mediana" or tamano_de_mascota == "Grande":
            if edad_de_mascota > edad_mas_vieja:
                edad_mas_vieja = edad_de_mascota
                tamano_de_mascota_mas_vieja = tamano_de_mascota
            
        
    
    #¿Su mascota esta vacunada?
    vacunada = input("\n¿Su mascota está vacunada?: \n[1]SI\n[2]NO\n\tElige una opcion: ")
    while vacunada != "1" and vacunada != "2":
        print("[ERROR] Opcion no valida.")
        vacunada = input("¿Su mascota está vacunada?: \n[1]SI\n[2]NO\n\tElige una opcion: ")
    vacunada = int(vacunada)
    if vacunada == 1:
        vacunada = "SI"
    elif vacunada == 2:
        vacunada = "NO"
    
    validacion = input("\nDesea continuar? [S] Sí - [CUALQUIER TECLA] No: ")
    if validacion.lower() != 's':
        print("Gracias por usar nuestro sistema. ¡Hasta luego!\n")
        break
    

#INFORMES
if edad_mas_vieja != None:
    print(f"\nLa mascota más vieja es de tamaño {tamano_de_mascota_mas_vieja}.")
else:
    print("\nNo se encontraron mascotas en los tamaños medianos o grandes.")
    
#B) Cuál es el promedio de edad de las gatas.

#C) Cuál es el tipo de mascota menos vacunado.

#D) El porcentaje de gatos, perros y otros.