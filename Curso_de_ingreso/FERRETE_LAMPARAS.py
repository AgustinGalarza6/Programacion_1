'''
Condicionales: Ferrete Lámparas.
En una ferretería se desea implementar un sistema que permita a los clientes conocer cuánto deben pagar por la compra de lámparas de bajo consumo. Cada lámpara tiene un costo fijo de $800.
El sistema debe aplicar los siguientes descuentos:
    Descuentos por Cantidad:
        6 o más lámparas: 50% de descuento.
        5 lámparas:
        Marca "ArgentinaLuz": 40% de descuento.
        Otras marcas: 30% de descuento.
        4 lámparas:
        Marca "ArgentinaLuz" o "FelipeLamparas": 25% de descuento.
        Otras marcas: 20% de descuento.
        3 lámparas:
        Marca "ArgentinaLuz": 15% de descuento.
        Marca "FelipeLamparas": 10% de descuento.
        Otras marcas: 5% de descuento.
    
    Descuento Adicional:
        Si el total con descuento supera los $4000, se aplica un descuento adicional del 5%.
    
    Salida del Sistema: El sistema debe mostrar la siguiente información en pantalla:
    Marca de las lámparas.
    Cantidad de lámparas compradas.
    Total a pagar sin descuento.
    Descuento aplicado (si corresponde).
    Descuento adicional (si corresponde).
    Total a pagar con descuentos aplicados.
'''

flag_descuento_adicional= False
coste_total = 0
coste_final = 0
descuento = 0
descuento_adicional = 0
porcentaje_descuento = 0
cantidad_de_lamparas = 0
costo_lampara = 800
marca_argentina_luz = "Argentina Luz"
marca_felipe_lamparas = "Felipe Lamparas"
marca_otros = "Otros"

menu = "SELECCIONE LA MARCA A COMPRAR\n\n[1] Argentina Luz\n[2] Felipe Lamparas\n[3] Otra marca\n\n[0] SALIR\n\n\tOPCION: "

marca = input(menu)
#Validacion
while marca != "1" and marca != "2" and marca != "3" and marca != "0":
    print("[ERROR] MARCA NO VALIDA")
    marca = input(menu)
#

if marca != "0":
    # MAPPEO LA OPCION CON EL LITERAL DE LA MARCA
    if marca == "1":
        marca = marca_argentina_luz
    else:
        if marca == "2":
            marca = marca_felipe_lamparas
        else:
            marca = marca_otros

    # PIDO CANTIDAD DE LAMPARAS A COMPRAR
    cantidad_de_lamparas = int(input("[+] INGRESE LA CANTIDAD DE LAMPARAS A COMPRAR: "))
    while cantidad_de_lamparas < 1:
        cantidad_de_lamparas = int(input("[ERROR] INGRESE LA CANTIDAD DE LAMPARAS A COMPRAR: "))

    # ACA EMPIEZA LA LOGICA DE DESCUENTOS
    if cantidad_de_lamparas >= 6:
        porcentaje_descuento = 0.5
    elif cantidad_de_lamparas == 5:
        if marca == marca_argentina_luz:
            porcentaje_descuento = 0.4
        else:
            porcentaje_descuento = 0.3
    elif cantidad_de_lamparas == 4:
        if marca == marca_argentina_luz or marca == marca_felipe_lamparas:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.2
    elif cantidad_de_lamparas == 3:
            if marca == marca_argentina_luz:
                porcentaje_descuento = 0.15
            elif marca == marca_felipe_lamparas:
                porcentaje_descuento = 0.1
            else:
                porcentaje_descuento = 0.05

    # CALCULO DE DESCUENTO POR CANTIDAD DE LAMPARAS Y MARCA
    coste_total = cantidad_de_lamparas * costo_lampara
    descuento = coste_total * porcentaje_descuento
    coste_final = coste_total - descuento

    # CALCULO DE DESCUENTO ADICIONAL 
    if coste_final > 4000:
        descuento_adicional = coste_final * 0.05
        coste_final -= descuento_adicional # coste_final = coste_final - descuento_adicional
        flag_descuento_adicional = True

    # INFORMES
    print(f"La marca elegida es: {marca}")
    print(f"La cantidad de lamparas compradas: {cantidad_de_lamparas}")    
    print(f"Coste total a pagar sin descuento: {coste_total}")  

    if porcentaje_descuento != 0:
        print(f"Descuento aplicado: {descuento}")  

    if descuento_adicional == True:
        print(f"Descuento adicional aplicado: {descuento_adicional}") 

    print(f"Total a pagar con descuentos aplicados: {coste_final}")

else:
    print("Gracias por elegirnos. ¡Hasta pronto!")
