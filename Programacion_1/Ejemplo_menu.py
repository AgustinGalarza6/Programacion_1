#EJ DE EXAMEN PARCIAL

"""
from Funciones import *         #IMPORTE DE FUNCIONES

calcular_promedio()
calcular_porcentaje()
calcular_suma()
calcular_division()

"""

respuesta = "N"
menu = '''
    A) Mostrar Promedio
    B) Mostrar Porcentajes
    C) Mostrar Suma
    D) Mostrar Division
    E) Salir
'''

while respuesta == "N":
    opcion_seleccionada = input(menu)
    match opcion_seleccionada:
        case "A":
            print("Resultados del promedio: ")
            #resultado_promedio = calcular_promedio()      IMPORT DE FUNCION
            #print(resultado_promedio)
        case "B":
            print("Resultados del porcentaje: ")
            #resultado_porcentaje = calcular_porcentaje()  IMPORT DE FUNCION
            #print(resultado_porcentaje)    
        case "C":
            print("Resultados del suma: ")
            #resultado_suma = calcular_suma()              IMPORT DE FUNCION
            #print(resultado_suma)    
        case "D":
            print("Resultados del suma: ")
            #resultado_division = calcular_division()      IMPORT DE FUNCION
            #print(resultado_division)       
        case "E":
            respuesta = input("Desea salir y terminar el programa? S/N")
        case _ : 
            print("La opcion ingresada no es correcta.")    