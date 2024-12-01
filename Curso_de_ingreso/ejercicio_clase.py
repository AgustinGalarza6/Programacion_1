#Encuesta de Empleados y Desempleados
#Descripción: Realizar una encuesta donde los encuestados elijan entre marca A, marca B o marca C. El programa debe:

#empleado_si_no
#voto
#edad

#Contar cuántos encuestados están empleados y cuántos no.
#Mostrar el porcentaje de votos de cada franquicia entre los empleados y los desempleados.
#Calcular el promedio de edad de los encuestados desempleados.

'''
ESTRUCTURA CORRECTA:

    CREAR VARIABLES
    PIDEN LOS DATOS (INPUT)
    VALIDAMOS LAS ENTRADAS
    RESUELVEN LOS PROBLEMAS
    INFORMES
    
'''


contador_empleado = 0
contador_desempleados = 0
acumulador_edad_desempleados = 0
contador_empleado_A = 0
contador_empleado_B = 0
contador_empleado_C = 0
contador_desempleado_A = 0
contador_desempleado_B = 0
contador_desempleado_C = 0


print("Bienvenidos a la encuesta\n")
print("A continuacion informenos si es empleado o no\n")

while True: 
    es_empleado = input("Escriba si es empleado o no: ")
    while es_empleado != "si" and es_empleado != "no":
        print("La respuesta no es valida")
        es_empleado = input("Escriba si es empleado o no: ")
        if es_empleado == "si":
            es_empleado = "es empleado"
        else: es_empleado = "no es empleado"

    voto = input("Escriba si su voto es por la marca A, B o C: ")
    while voto != "A" and voto != "B" and voto != "C":
        print("La respuesta no es valida")
        voto = input("Escriba si su voto es por la marca A, B o C: ")
        if voto == "A" or "a":
            voto = "marca A"
        elif voto == "marca B or b":
            voto = "por la marca B"
        else: voto = "marca C or c"


    edad = input("Escriba su edad: ")
    while not edad.isdigit():
        print("La edad no es valida")
        edad = input("Escriba su edad: ")
    edad = int(edad)
    # Acumulador de edades para sacar promedio
    acumulador_edad_desempleados += edad


    #Verificamos si es empleado o no
    if es_empleado == "si":
        contador_empleado += 1
        if voto == "A":
            contador_empleado_A += 1
        elif voto == "B":
            contador_empleado_B += 1
        elif voto == "C":
            contador_empleado_C += 1
    else:
        contador_desempleados += 1
        if voto == "A":
            contador_desempleado_A += 1
        elif voto == "B":
            contador_desempleado_B += 1
        elif voto == "C":
            contador_desempleado_C += 1
            
    continuar = input("¿Desea continuar con otra encuesta? (si/no): ")
    if (continuar != "si") or (continuar != "Si") or (continuar != "SI"):
        break


#INFORMES

#Contar cuántos encuestados están empleados y cuántos no.
print(f"El total de encuestados es de: {contador_empleado + contador_desempleados}")
print(f"Los encuestados empleados son: {contador_empleado} y los desempleados son: {contador_desempleados}")

# Mostrar el porcentaje de votos de cada franquicia entre los empleados y los desempleados.
# EMPLEADOS
if contador_empleado > 0:
    porcentaje_A = (contador_empleado_A / contador_empleado) * 100
    porcentaje_B = (contador_empleado_B / contador_empleado) * 100
    porcentaje_C = (contador_empleado_C / contador_empleado) * 100      
    print(f"La porcentaje de votos de los empleados por la marca A es: {porcentaje_A}%, por la marca B es: {porcentaje_B}%, y por la marca C es: {porcentaje_C}%")
else: print("No se han realizado encuestas de empleados")
#DESEMPLEADOS
if contador_desempleados > 0:
    porcentaje_A_desempleados = (contador_desempleado_A / contador_desempleados) * 100
    porcentaje_B_desempleados = (contador_desempleado_B / contador_desempleados) * 100
    porcentaje_C_desempleados = (contador_desempleado_C / contador_desempleados) * 100
    print(f"La porcentaje de votos de los desempleados por la marca A es: {porcentaje_A_desempleados}%, por la marca B es: {porcentaje_B_desempleados}%, y por la marca C es: {porcentaje_C_desempleados}%")
else:
    print("No se han realizado encuestas de desempleados")

#Calcular el promedio de edad de los encuestados desempleados.
if contador_desempleados > 0:
    print(f"El promedio de edad de los encuestados desempleados es: {acumulador_edad_desempleados / contador_desempleados}")
else:
    print("No se ingresaron encuestados desempleados")