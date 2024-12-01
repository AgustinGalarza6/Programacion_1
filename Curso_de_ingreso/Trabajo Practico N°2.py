"""
Enunciado:
De los 3 Jugadores de un Reality Show, se registra:
El nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos

Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.

# Todos los datos se ingresan mediante input()
"""

print("Bienvenidos al Reality Show")
max_votos = float('-inf')
min_votos = float('inf')
participant_mas_votado = ""
participant_menos_votado = ""
participant_menos_votado_edad = 0
total_de_votos = 0
total_edades = 0


#-------------------------

# Ingreso de datos del primer participante

participante_1 = input("Ingresa el nombre del primer participante: ")
participante_1_edad = int(input("Ingresa la edad del primer participante (mayor o igual a 25 años): "))
while participante_1_edad < 25:
    print("La edad del participante debe ser mayor o igual a 25 años.")
    participante_1_edad = int(input("Por favor. Ingrese la edad del primer participante nuevamente: "))
    
participante_1_votos = int(input("Ingresa la cantidad de votos del primer participante (mayor o igual a 0): "))
while participante_1_votos < 0:
    print("La cantidad de votos no puede ser menor a 0.")
    participante_1_votos = int(input("Ingresa la cantidad de votos del primer participante (mayor o igual a 0): "))
    
# Actualización de máximos y mínimos votos
if participante_1_votos > max_votos:
    max_votos = participante_1_votos
    participant_mas_votado = participante_1

if participante_1_votos < min_votos:
    min_votos = participante_1_votos
    participant_menos_votado = participante_1
    participant_menos_votado_edad = participante_1_edad

# Suma de votos y edades totales
total_de_votos += participante_1_votos
total_edades += participante_1_edad

    
#-------------------------

# Ingreso de datos del segundo participante

participante_2 = input("Ingresa el nombre del segundo participante: ")
participante_2_edad = int(input("Ingresa la edad del segundo participante (mayor o igual a 25): "))
while participante_2_edad < 25:
    print("La edad del participante debe ser mayor o igual a 25 años.")
    participante_2_edad = int(input("Por favor. Ingrese la edad del segundo participante nuevamente: "))

participante_2_votos = int(input("Ingresa la cantidad de votos del segundo participante (mayor o igual a 0): "))
while participante_2_votos < 0:
    print("La cantidad de votos no puede ser menor a 0, ingrese los votos nuevamente")
    participante_2_votos = int(input("Por favor. Ingrese los votos del segundo participante nuevamente: "))

# Actualización de máximos y mínimos votos
if participante_2_votos > max_votos:
    max_votos = participante_2_votos
    participant_mas_votado = participante_2

if participante_2_votos < min_votos:
    min_votos = participante_2_votos
    participant_menos_votado = participante_2
    participant_menos_votado_edad = participante_2_edad

# Suma de votos y edades totales
total_de_votos += participante_2_votos
total_edades += participante_2_edad


#-------------------------

# Ingreso de datos del tercer participante

participante_3 = input("Ingresa el nombre del tercer participante: ")
participante_3_edad = int(input("Ingresa la edad del tercer participante (mayor o igual a 25): "))
while participante_3_edad < 25:
    print("La edad del participante debe ser mayor o igual a 25 años.")
    participante_3_edad = int(input("Por favor. Ingrese la edad del tercer participante nuevamente: "))

participante_3_votos = int(input("Ingresa la cantidad de votos del tercer participante (mayor o igual a 0): "))
while participante_3_votos < 0:
    print("La cantidad de votos no puede ser menor a 0, ingrese los votos nuevamente")
    participante_3_votos = int(input("Por favor. Ingrese la cantidad de votos del tercer participante nuevamente: "))
    
# Actualización de máximos y mínimos votos
if participante_3_votos > max_votos:
    max_votos = participante_3_votos
    participant_mas_votado = participante_3

if participante_3_votos < min_votos:
    min_votos = participante_3_votos
    participant_menos_votado = participante_3
    participant_menos_votado_edad = participante_3_edad

# Suma de votos y edades totales
total_de_votos += participante_3_votos
total_edades += participante_3_edad


#-------------------------   

# Cálculo del promedio de edades
promedio_de_edad = total_edades / 3

# Informaciones solicitadas del TP
print("RESULTADOS:")
print("a. Nombre del candidato con más votos es :", participant_mas_votado)
print("b. Nombre y edad del candidato con menos votos es :", participant_menos_votado, "(Y tiene: ", participant_menos_votado_edad,"años)")
print("c. Promedio de edades de los candidatos:", promedio_de_edad)
print("d. Total de votos emitidos:", total_de_votos)