#Condicionales:
#Ferrete Lámparas

#En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de #bajo consumo.
#Se tiene en cuenta que todas las lámparas cuestan $800.

#Se aplicará el siguiente descuento:
#Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
#Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
#Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el #descuento es del 20%.
#Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % #y si es de otra marca un 5%.

#Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

#Mostrar por pantalla: 
#Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) #y el total a pagar con descuento.


# Def variables
precio_de_las_lamparas = int(800)
cant_de_lamparas = int(input("Cuantas lamparas quiere?: "))
precio_total = cant_de_lamparas * precio_de_las_lamparas
descuento = precio_total * 0.5 # Osea el subtotal * 0.5 que seria su %50
total_a_pagar = precio_total - descuento
marca_de_lampara = input("Que marca va a llevar?: ")
marca_1 = "ArgentinaLuz"
marca_2 = "FelipeLamparas"
resultado = float
precio_con_descuento_extra = float


# Si el cliente quiere llevar 6 o mas lamparas, se le descuenta un %50
if cant_de_lamparas >= 6:
    precio_total = cant_de_lamparas * precio_de_las_lamparas # Seria por ejemplo 6*800 = 4800
    descuento = precio_total * 0.5
    total_a_pagar = precio_total - descuento
    print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
    print("\tMarca:",marca_de_lampara)
    print("\tEl precio total es: ", precio_total)
    print("\tEl descuento es: ", descuento)
    print("\tEl total a pagar es: ", total_a_pagar)
    
    if total_a_pagar > 4000:
        resultado = total_a_pagar * 0.05
        precio_con_descuento_extra = total_a_pagar - resultado
        print("\nDebido a que el precio con el descuento sigue excediendo los $4000 se le aplicara un %5 extra de descuento: \n\tEl descuento extra es: ", resultado, "\n\tEl precio final es: ", precio_con_descuento_extra)
        
        

# Si el cliente quiere llevar 5 lamparas, se le descuenta un %40 "SI ES ARGENTINA LUZ" y si es felipeLamparas un %30
if cant_de_lamparas == 5:
    precio_total = cant_de_lamparas * precio_de_las_lamparas
    if marca_de_lampara == marca_1:
        descuento = precio_total * 0.4
        total_a_pagar = precio_total - descuento
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)
        
    elif marca_de_lampara == marca_2:
        descuento = precio_total * 0.3
        total_a_pagar = precio_total - descuento
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)
        
        

#Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el #descuento es del 20%.
if cant_de_lamparas == 4:
    precio_total = cant_de_lamparas * precio_de_las_lamparas
    if (marca_de_lampara == marca_1) or (marca_de_lampara == marca_2):
        descuento = precio_total * 0.25
        total_a_pagar = precio_total - descuento
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)
        
    else:
        descuento = precio_total * 0.20
        total_a_pagar = precio_total - descuento
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)
        
        
        
#Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % #y si es de otra marca un 5%.
if cant_de_lamparas == 3:
    precio_total = cant_de_lamparas * precio_de_las_lamparas
    if marca_de_lampara == marca_1:
        descuento = precio_total * 0.15
        total_a_pagar = precio_total - descuento
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)
    elif marca_de_lampara == marca_2:
        descuento = precio_total * 0.10
        total_a_pagar = precio_total - descuento
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)
    else:
        descuento = precio_total * 0.05
        print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
        print("\tMarca:",marca_de_lampara)
        print("\tEl precio total es: ", precio_total)
        print("\tEl descuento es: ", descuento)
        print("\tEl total a pagar es: ", total_a_pagar)