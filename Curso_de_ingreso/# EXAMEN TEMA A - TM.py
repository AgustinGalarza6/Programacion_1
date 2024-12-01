#UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
#franquicia que se insertará en el mercado argentino y en la cual invertirán.
#Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
#Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
#propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):

#Se ingresa de cada encuestado:
#● nombre
#● edad (no menor a 18)
#● está empleado (si-no)
#● género (Masculino - Femenino - Otro)
#● voto (APPLE, DUNKIN, IKEA)

#Se necesita saber:
#1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive.
#2. Nombre y voto del encuestado de género Masculino con menor edad.
#3. Porcentaje de votos de cada género.
#4. Promedio de edad de los encuestados de género Femenino que votaron IKEA.
#5. Determinar cuál fue el género que tuvo más 

encuestadosvalidacion = "s"
nombre_del_votante = ""
edad_del_votante = ""
genero_del_votante = ""
cantidad_de_encuestados_desempleados = 0
votante_masculino_mas_joven = None
nombre_del_votante_mas_joven = None
voto_del_mas_joven = None
contador_de_personas = 0
acumulador_edad_femenino = 0
encuestados_otro = 0
encuestados_man = 0
encuestados_fem = 0
encuestadas_femeninas_IKEA = 0

while validacion == "s" or "S":
    
    # Preguntamos si es empleado:
    es_empleado = input("[1] Empleado\n[2] Desempleado\nIngrese una opcion: ")
    while (es_empleado != "1") and (es_empleado != "2"):
        print("Respuesta no valida")
        es_empleado = input("[1] Empleado\n[2] Desempleado\nIngrese una opcion: ")
    # Verificamos si es empleado
    if es_empleado == "1":
        es_empleado = "empleado"
    else:
        es_empleado = "desempleado"
    
    # Capturamos el nombre del votante
    nombre_del_votante = input("Ingrese su nombre: ")
    while not nombre_del_votante.isalpha():
        print("Nombre no valido")
        nombre_del_votante = input("Ingrese de nuevo el nombre: ")

    # Capturamos la edad
    edad_del_votante = input("Ingrese su edad: ")
    while not edad_del_votante.isdigit() or (edad_del_votante < 18):
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
        encuestados_man += 1
    elif genero_del_votante == "2":
        genero_del_votante = "Femenino"
        encuestados_fem += 1
    else:
        genero_del_votante = "Otro genero"
        encuestados_otro += 1
    
    # Capturamos el voto del votante
    voto = input("Voto: \n[1] APPLE\n[2] DUNKIN\n[3] IKEA\nIngrese una opcion: ")
    while not voto.isdigit() or int(voto) > 3 or int(voto) < 1:
        print("Voto no valido")
        voto = input("Ingrese de nuevo el voto: ")
    
    if voto == "1":
        voto = "APPLE"
    elif voto == "2":
        voto = "DUNKIN"
    else:
        voto = "IKEA"
        if genero_del_votante == "Femenino":
            acumulador_edad_femenino += edad_del_votante
            encuestadas_femeninas_IKEA += 1
    
    # Encuestados desempleados que votaron por DUNKIN o IKEA
    if (es_empleado == "desempleado") and (voto == "DUNKIN" or voto == "IKEA") and (edad_del_votante >= 25 and edad_del_votante <= 50):
        cantidad_de_encuestados_desempleados += 1

    # Buscamos el votante más joven dentro de los masculinos
    if genero_del_votante == "Masculino":
        if (votante_masculino_mas_joven == None) or (edad_del_votante < votante_masculino_mas_joven):
            votante_masculino_mas_joven = edad_del_votante
            nombre_del_votante_mas_joven = nombre_del_votante
            voto_del_mas_joven = voto
    
    validacion = input("\nDesea continuar? [S] Si - [CUALQUIER TECLA] No: ")
    
    contador_de_personas += 1

# INFORMES

# 1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive.
print(f"La cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive es {cantidad_de_encuestados_desempleados}.")

# 2. Nombre y voto del encuestado de género Masculino con menor edad.
if votante_masculino_mas_joven != None:
    print(f"El encuestado de género Masculino con menor edad es {nombre_del_votante_mas_joven} y voto a: {voto_del_mas_joven}.")
else:
    print("No se encontraron votantes de género masculino con menor edad.")
    
# 3. Porcentaje de votos de cada género.
if contador_de_personas > 0:
    porcentaje_masculino = (encuestados_man * 100) / contador_de_personas
    print(f"El porcentaje de votos de género Masculino es {porcentaje_masculino}%.")
    
    porcentaje_femenino = (encuestados_fem * 100) / contador_de_personas
    print(f"El porcentaje de votos de género Femenino es {porcentaje_femenino}%.")
    
    porcentaje_otro = (encuestados_otro * 100) / contador_de_personas
    print(f"El porcentaje de votos de género Otro género es {porcentaje_otro}%.")
    

# 4. Promedio de edad de los encuestados de género Femenino que votaron IKEA.
if encuestadas_femeninas_IKEA > 0:
    promedio_edad_femenino = acumulador_edad_femenino / encuestadas_femeninas_IKEA
    print(f"El promedio de edad de los encuestados de género Femenino que votaron IKEA es {promedio_edad_femenino}.")
else:
    print("No se encontraron encuestados de género Femenino que votaron IKEA.")

# 5. Determinar cuál fue el género que tuvo más encuestados.
if (encuestados_man > encuestados_fem) and (encuestados_man > encuestados_otro):
    print(f"El género que tuvo más encuestados es el género: Masculino.")
elif (encuestados_fem > encuestados_man) and (encuestados_fem > encuestados_otro):
    print(f"El género que tuvo más encuestados es el género: Femenino.")
elif (encuestados_otro > encuestados_man) and (encuestados_otro > encuestados_fem):
    print(f"El género que tuvo más encuestados es el género: Otro género.")
else:
    print("Hay un empate en la cantidad de encuestados entre los géneros.")