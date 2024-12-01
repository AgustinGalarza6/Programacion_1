# Ejemplo
#Listen los nombres de los que sean mayores a 20 años... 
#Si hay dos que lo cumplen, tienen que mostrar Maria, José

nombre = ""
edad= ""
nombre_guardado = None
Edad_guardada = None
validacion = 's'

#Solicitamos nombres
while validacion == "s" or "S":
    nombre = input("Nombre del jugador: ")
    while not nombre.isalpha():
        print("Nombre no válido.")
        nombre_del_jugador = input("Ingrese de nuevo el nombre: ")

    edad = input("¿Qué edad tiene? (no menor a 18): ")
    while not edad.isdigit():
        print("Edad no válida.")
        edad = input("Ingrese de nuevo la edad: ")
    edad = int(edad)
    if edad > 20:
        if nombre_guardado is None:
            nombre_guardado = nombre
            Edad_guardada = edad
    
    validacion = input("\nDesea continuar? [S] Si - [CUALQUIER TECLA] No: ")
    if validacion != 's' and validacion != 'S':
        print("Chau!\n")
        break
        
    
# INFORME
print('Informes')

#A) Si hay dos nombres, mostrar Maria, José
if nombre_guardado != None and Edad_guardada != None:
    print(f'Si hay dos nombres, {nombre_guardado} y {Edad_guardada} ')
    
    