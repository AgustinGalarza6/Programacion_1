#PUNTO 3
#En una carga indefinida de datos (hasta que el usuario quiera) se desea llevar a cabo el registro diario de una #granja de minería en Bitcoin y Ethereum.
#Se requieren los siguientes datos:
#Nombre de la criptomoneda (VALIDAR EL INGRESO solo de BTC o ETH).
#Cantidad de BTC o ETH minado ese día - Número positivo.
#Valor en USD de la unidad cripto en el día - Número positivo inclusive 0. (Multiplicar valor unitario x Cantidad #minada)

#INFORMAR

#A) Nombre y cantidad de la criptomoneda más minada.
#B) Nombre de la criptomoneda que mayor cotización tuvo.
#C) Cantidad total de ingreso bruto en USD de cada criptomoneda.
#D) Sabiendo que el coste de electricidad para BTC es de un 7% y para ETH es un 4% calcular el ingreso total neto #en USD.
#E) Convertir el ingreso neto en ARS solo para ETH. 

#Sabiendo que la cotización de 1 USD a ARS es de $1430.
#Si el ingreso supera los 100.000 ARS calcular impuesto de AFIP del 21% e informar
#"El ingreso neto por ETH es de {X1} pesos y se descontó {X2} pesos de AFIP". Siendo X1 el neto en ARS y X2 el #impuesto aplicado.

minado_BTC = 0
minado_ETH = 0
acum_cotizacion_USD_BTC = 0
acum_cotizacion_USD_ETH = 0
moneda_max = None
porcentaje_coste_electricidad_btc = 0.07 # %7
porcentaje_coste_electricidad_eth = 0.04 # %4
ingreso_neto_BTC = 0
ingreso_neto_ETH = None
ingreso_bruto_BTC = None
ingreso_bruto_ETH = None
ingreso_neto_ARS = None
cotizacion_ARS = 1430
impuesto_AFIP = None
porcentaje_AFIP = 0.21 # %21
validacion = "s"

while validacion == "s" or "S":
    #Nombre de la criptomoneda (VALIDAR EL INGRESO solo de BTC o ETH).
    Nombre_crypto = input("Ingresa el nombre de la criptomoneda (BTC o ETH): ")
    while Nombre_crypto != "BTC" and Nombre_crypto != "ETH":
        print("Opción no válida")
        Nombre_crypto = input("Ingresa el nombre de la criptomoneda (BTC o ETH): ")
    
    
    #Cantidad de BTC o ETH minado ese día - Número positivo.
    minado_dia = float(input("Ingresa la cantidad de BTC o ETH minado ese día: "))
    while minado_dia < 0:
        print("La cantidad no puede ser negativa")
        minado_dia = float(input("Ingresa la cantidad de BTC o ETH minado ese día: "))
    
    #Valor en USD de la comunidad cripto en el día - Número positivo inclusive 0. (Multiplicar valor unitario x Cantidad #minada)
    valor_USD = float(input("Ingresa el valor de la unidad cripto en el día: "))
    while valor_USD < 0:
        print("El valor no puede ser negativo")
        valor_USD = float(input("Ingresa el valor de la unidad cripto en el día: "))
    
     # Acumulación de datos
    if Nombre_crypto == "BTC":
        minado_BTC += minado_dia
        acum_cotizacion_USD_BTC += valor_USD * minado_dia
    else:
        minado_ETH += minado_dia
        acum_cotizacion_USD_ETH += valor_USD * minado_dia
    
    #Preguntamos si el usuario desea continuar o no
    validacion = input("\nDesea continuar? [S] Sí - [CUALQUIER TECLA] No: ")
    if validacion != "S" and validacion != "s":
        print("Gracias por usar nuestro sistema de inversiones. ¡Hasta luego!\n")
        break
        
#INFORMES
#A) Nombre y cantidad de la criptomoneda más minada.
print("INFORME 1")
if minado_BTC > minado_ETH:
    print(f"La cryptomoneda mas minada es BTC, con un total de: {minado_BTC} USD")
else:
    print(f"La cryptomoneda mas minada es ETH, con un total de: {minado_ETH} USD")
    
#B) Nombre de la criptomoneda que mayor cotización tuvo.
if acum_cotizacion_USD_BTC > acum_cotizacion_USD_ETH:
    print(f"La criptomoneda que mayor cotizacion tuvo es BTC, con una cotizacion de: {acum_cotizacion_USD_BTC}")
else:
    print(f"La criptomoneda que mayor cotizacion tuvo es ETH, con una cotizacion de: {acum_cotizacion_USD_ETH}")

#C) Cantidad total de ingreso bruto en USD de cada criptomoneda.
if acum_cotizacion_USD_BTC > 0:
    print(f"El ingreso bruto en USD de BTC es ${acum_cotizacion_USD_BTC}")
else:
    print("No se registraron ingresos en BTC")

if acum_cotizacion_USD_ETH > 0:
    print(f"El ingreso bruto en USD de ETH es ${acum_cotizacion_USD_ETH}")
else:
    print("No se registraron ingresos en ETH")

#D) Sabiendo que el coste de electricidad para BTC es de un 7% y para ETH es un 4% calcular el ingreso total neto #en USD.
ingreso_neto_BTC = acum_cotizacion_USD_BTC * (1 - porcentaje_coste_electricidad_btc)
ingreso_neto_ETH = acum_cotizacion_USD_ETH * (1 - porcentaje_coste_electricidad_eth)
if ingreso_neto_BTC > 0:
    print(f"El ingreso neto en USD de BTC es ${ingreso_neto_BTC}")
else:
    print("No se registraron ingresos en BTC")

if ingreso_neto_ETH > 0:
    print(f"El ingreso neto en USD de ETH es ${ingreso_neto_ETH}")
else:
    print("No se registraron ingresos en ETH")

#E) Convertir el ingreso neto en ARS solo para ETH.
if ingreso_neto_ETH > 0:
    ingreso_neto_ARS = (ingreso_neto_ETH * cotizacion_ARS)
    print(f"El ingreso neto en ARS de ETH es {ingreso_neto_ARS}")
else:
    print("No se registraron inversiones en ETH")
    

#Sabiendo que la cotización de 1 USD a ARS es de $1430.
#Si el ingreso supera los 100.000 ARS calcular impuesto de AFIP del 21% e informar
#"El ingreso neto por ETH es de {X1} pesos y se descontó {X2} pesos de AFIP". Siendo X1 el neto en ARS y X2 el #impuesto aplicado.
if (ingreso_neto_ARS != None) and (ingreso_neto_ARS > 100000):
    impuesto_AFIP = (ingreso_neto_ARS * porcentaje_AFIP)
# El ingreso neto por ETH es de {X1} pesos y se descontó {X2} pesos de AFIP". Siendo X1 el neto en ARS y X2 el #impuesto aplicado.
    print(f"El ingreso neto por ETH es de {ingreso_neto_ARS} pesos y se descontó {porcentaje_AFIP} pesos de AFIP.") 
else:
    print("No se aplicaron impuestos")