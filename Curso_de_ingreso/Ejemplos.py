#print ("Bienvenidos a CTC Sistemas: ")

#nombre = (input("¿Cual es tu nombre?: "))
#print("Bienvenido: ",nombre)

#print("Con que departamento desea comunicarse?: ")
#print("[1] Sistemas")
#print("[2] Facturaciones")
#print("[3] Area de pedidos")

#opcion = int(input("Ingresa una opcion: "))

#if(opcion == 1):
    #print("Hola ", nombre, " bienvenido al departamento de CTC Sistemas")
#elif(opcion == 2):
    #print("Hola ", nombre, " bienvenido al departamento de Facturaciones")
#elif(opcion == 3):
    #print("Hola ", nombre, " bienvenido al departamento de Area de pedidos")
#else:
    #print("Opcion invalida")


#match case
    #case 1:
        #print("Hola ", nombre, " bienvenido al departamento de CTC Sistemas")
    #case 2:
        #print("Hola ", nombre, " bienvenido al departamento de Facturaciones")
    #case 3:
        #print("Hola ", nombre, " bienvenido al departamento de Area de pedidos")
    #case _:
        #print("Opcion invalida")



#Crear un programa que pida al usuario un número, si coincide con el valor
#18, mostrar el mensaje “Usted tiene 18 años”.

numero_ingresado = int(input("Ingresa un numero: "))

if (numero_ingresado == 18):
    print("Usted tiene 18 años")
else:
    print("Usted no tiene 18 años")
    
    
#Crear un programa que pida al usuario un número y pueda calcular si es o
#no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso
#contrario “MENOR”

Edad_usuario = int(input("Ingresa tu edad: "))

if (Edad_usuario >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted es Menor de edad")


#Crear un programa que a partir del ingreso de la altura de un
#basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
#medir más de 1.80 metros

altura_usuario = float(input("Ingresa tu altura: "))

if (altura_usuario <= 1.80): 
    print("Para ser pivot debes medir mas de 1.80 metros")
else:
    print("Sos apto par jugar de pivot")
    

#Crear un programa que se ingrese la edad del usuario en número y pueda
#calcular si es adolescente (edad entre 13 y 17 años).

edad_del_usuario = int(input("Ingresa tu edad: "))

if (edad_del_usuario >= 13 and edad_del_usuario <= 17):
    print("Usted es adolescente")
else:
    print("Usted no es adolescente")
    

#Crear un programa que al ingresar un número puede calcular si es mayor,
#niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
#adolescente (edad entre 13 y 17 años) de edad.

Edad_usuario = int(input("Ingresa tu edad: "))

if (Edad_usuario < 10):
    print("Usted es un niño")
elif (Edad_usuario >= 10 and Edad_usuario <= 13):
    print("Usted es un pre-adolescente")
elif (Edad_usuario >= 13 and Edad_usuario <= 17):
    print("Usted es un adolescente")
else:
    print("Usted es mayor")