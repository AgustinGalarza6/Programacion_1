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

altura_usuario = float(input("Ingresa tu altura en metros: "))

if (altura_usuario > 1.80): 
    print("Sos apto para jugar de pivot")
else:
    print("Para ser pivot debes medir más de 1.80 metros")

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
    print("Usted es mayor de edad")
