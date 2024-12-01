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
#Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

# vamos a crear un menú interactivo para que el usuario pueda ingresar cuantas y que marca de lamparas quiere:


while True:
    print("--------------------- Bienvenido a Ferretería El Negraso ---------------------")
    print('\n')
    # Ingreso de datos
    cant_de_lamparas = int(input("Cuantas lamparas quiere?: "))
    print("\n")
    print("Las marcas de lamparas disponibles son: \n 1. ArgentinaLuz \n 2. FelipeLamparas \n 3. Otra Marca \n")
    marca_de_lampara = input('A continuación elija la marca de lampara que va a llevar utilizando los numeros 1, 2 o 3: ')

    # Def variables conocidas por el programa
    precio_de_las_lamparas = int(800)
    marca_1 = "ArgentinaLuz"
    marca_2 = "FelipeLamparas"
    marca_3 = "Otra Marca"

    # Mostrar marca de lampara en caso de que elija 1, 2 o 3

    while marca_de_lampara != '1' or marca_de_lampara != '2' or marca_de_lampara != '3':
        print("Opcion no valida. Por favor, ingrese otro valor.")
        marca_de_lampara = input('Ingrese una opcion valida: 1, 2 o 3: ')

    if marca_de_lampara == '1':
        marca_de_lampara = marca_1
    elif marca_de_lampara == '2':
        marca_de_lampara = marca_2
    elif marca_de_lampara == '3':
        marca_de_lampara = marca_3
        

    # Si el cliente quiere llevar 6 o mas lamparas, se le descuenta un %50
    if cant_de_lamparas >= 6:
        precio_total = cant_de_lamparas * precio_de_las_lamparas # Seria por ejemplo 6*800 = 4800
        descuento = precio_total * 0.5
        total_a_pagar = precio_total - descuento
        print(f"\nEl cliente se lleva un total de {cant_de_lamparas} lamparas.")
        print(f"\tMarca: {marca_de_lampara}")
        print(f"\tEl precio total es de: {precio_total}")
        print(f"\tEl descuento es de: {descuento}")
        print(f"\tEl total a pagar con descuento aplicado es de: {total_a_pagar}")
        
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
            total_a_pagar = precio_total - descuento
            print("\nEl cliente se lleva:",cant_de_lamparas,"lamparas en total.")
            print("\tMarca:",marca_de_lampara)
            print("\tEl precio total es: ", precio_total)
            print("\tEl descuento es: ", descuento)
            print("\tEl total a pagar es: ", total_a_pagar)
        
    respuesta = input("\n¿Desea realizar otro pedido? (s/n): ")
    if respuesta == "n":
        print("\nGracias por su compra en ferreteria 'El Negraso'.")
        break