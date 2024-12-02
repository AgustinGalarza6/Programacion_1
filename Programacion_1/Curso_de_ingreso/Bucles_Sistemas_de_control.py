#Bucles: Sistema de Control de Gastos Semanales.
#Registrar gastos diarios durante una semana y luego calcular el total de gastos, el gasto promedio diario, el día con mayor gasto y el día con menor gasto. El programa debe utilizar un bucle while para
#solicitar los gastos diarios, así como contadores y acumuladores para realizar los cálculos necesarios.

#El programa debe solicitar al usuario ingresar los gastos diarios durante 7 días.
#Utiliza un bucle while para ingresar los gastos.
#Utiliza contadores y acumuladores para calcular:

#El total de gastos de la semana.
#El gasto promedio diario.
#El día con el mayor gasto.
#El día con el menor gasto.

#Al final, muestra en pantalla los resultados. Mostrar día con el valor literal, ej: “Lunes”, “Martes”, etc.

dia = 0
acumulador = 0
dia_literal = ""
mayor_gasto = 0
menor_gasto = 0 
dia_mayor_gasto = 0
dia_menor_gasto = 0
msj_gastos_diarios = ""

while dia < 7:
    gasto = int(input("Ingresa el gasto del dia: "))
    acumulador += gasto
    match dia:
        case 0:
            msj_gastos_diarios += f"Lunes - Gasto: {gasto}\n"
        case 1:
            msj_gastos_diarios += f"Martes - Gasto: {gasto}\n"
        case 2:
            msj_gastos_diarios += f"Miercoles - Gasto: {gasto}\n"
        case 3:
            msj_gastos_diarios += f"Jueves - Gasto: {gasto}\n"
        case 4:
            msj_gastos_diarios += f"Viernes - Gasto: {gasto}\n"
        case 5:
            msj_gastos_diarios += f"Sabado - Gasto: {gasto}\n"
        case 6:
            msj_gastos_diarios += f"Domingo - Gasto: {gasto}\n"
        
    if dia == 0 or gasto > mayor_gasto:
        dia_mayor_gasto = dia
        mayor_gasto = gasto
    if dia == 0 or gasto < menor_gasto:
        dia_menor_gasto = dia
        menor_gasto = gasto
    dia += 1
    
    # Dia con el mayor gasto
    match dia_mayor_gasto:
        case 0:
            dia_mayor_gasto = "Lunes"
        case 1:
            dia_mayor_gasto = "Martes"
        case 2:
            dia_mayor_gasto = "Miercoles"
        case 3:
            dia_mayor_gasto = "Jueves"
        case 4:
            dia_mayor_gasto = "Viernes"
        case 5:
            dia_mayor_gasto = "Sabado"
        case 6:
            dia_mayor_gasto = "Domingo"
    
    # Dia con el menor gasto
    match dia_menor_gasto:
        case 0:
            dia_menor_gasto = "Lunes"
        case 1:
            dia_menor_gasto = "Martes"
        case 2:
            dia_menor_gasto = "Miercoles"
        case 3:
            dia_menor_gasto = "Jueves"
        case 4:
            dia_menor_gasto = "Viernes"
        case 5:
            dia_menor_gasto = "Sabado"
        case 6:
            dia_menor_gasto = "Domingo"
        
# Informes
print(f"Gasto de la semana: {acumulador}")
print(f"Gasto promedio diario: {acumulador / 7}")
print(f"El dia con el mayor gasto es: {dia_mayor_gasto} y fue de ${mayor_gasto}")
print(f"El dia con el menor gasto es: {dia_menor_gasto} y fue de ${menor_gasto}")