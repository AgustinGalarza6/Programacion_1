print("Bienvenidos al Reality Show")

# Definicion de variables
max_votes = -1
min_votes = float('inf')
participant_most_votes = ""
participant_least_votes = ""
total_votes = 0
total_age = 0

# Datos del primer participante
participante_1 = input("Ingresa el nombre del primer participante: ")
participante_1_edad = int(input("Ingresa la edad del primer participante (mayor o igual a 25): "))
while participante_1_edad < 25:
    print("La edad debe ser mayor o igual a 25.")
    participante_1_edad = int(input("Ingresa la edad del primer participante (mayor o igual a 25): "))
participante_1_votos = int(input("Ingresa la cantidad de votos del primer participante (mayor o igual a 0): "))
while participante_1_votos < 0:
    print("La cantidad de votos no puede ser menor a 0.")
    participante_1_votos = int(input("Ingresa la cantidad de votos del primer participante (mayor o igual a 0): "))

# Update max and min votes
if participante_1_votos > max_votes:
    max_votes = participante_1_votos
    participant_most_votes = participante_1
if participante_1_votos < min_votes:
    min_votes = participante_1_votos
    participant_least_votes = participante_1

# Update total votes and total age
total_votes += participante_1_votos
total_age += participante_1_edad

# Input for participant 2
participant_2 = input("Ingresa el nombre del segundo participante: ")
participant_2_edad = int(input("Ingresa la edad del segundo participante (mayor o igual a 25): "))
while participant_2_edad < 25:
    print("La edad debe ser mayor o igual a 25.")
    participant_2_edad = int(input("Ingresa la edad del segundo participante (mayor o igual a 25): "))
participant_2_votos = int(input("Ingresa la cantidad de votos del segundo participante (mayor o igual a 0): "))
while participant_2_votos < 0:
    print("La cantidad de votos no puede ser menor a 0.")
    participant_2_votos = int(input("Ingresa la cantidad de votos del segundo participante (mayor o igual a 0): "))

# Update max and min votes
if participant_2_votos > max_votes:
    max_votes = participant_2_votos
    participant_most_votes = participant_2
if participant_2_votos < min_votes:
    min_votes = participant_2_votos
    participant_least_votes = participant_2

# Update total votes and total age
total_votes += participant_2_votos
total_age += participant_2_edad

# Input for participant 3
participant_3 = input("Ingresa el nombre del tercer participante: ")
participant_3_edad = int(input("Ingresa la edad del tercer participante (mayor o igual a 25): "))
while participant_3_edad < 25:
    print("La edad debe ser mayor o igual a 25.")
    participant_3_edad = int(input("Ingresa la edad del tercer participante (mayor o igual a 25): "))
participant_3_votos = int(input("Ingresa la cantidad de votos del tercer participante (mayor o igual a 0): "))
while participant_3_votos < 0:
    print("La cantidad de votos no puede ser menor a 0.")
    participant_3_votos = int(input("Ingresa la cantidad de votos del tercer participante (mayor o igual a 0): "))

# Update max and min votes
if participant_3_votos > max_votes:
    max_votes = participant_3_votos
    participant_most_votes = participant_3
if participant_3_votos < min_votes:
    min_votes = participant_3_votos
    participant_least_votes = participant_3

# Update total votes and total age
total_votes += participant_3_votos
total_age += participant_3_edad

# Calculate average age
average_age = total_age / 3

# Output results
print("a. Nombre del candidato con más votos:", participant_most_votes)
print("b. Nombre y edad del candidato con menos votos:", participant_least_votes, "(edad:", participante_1_edad, ")")
print("c. Promedio de edades de los candidatos:", average_age)
print("d. Total de votos emitidos:", total_votes)