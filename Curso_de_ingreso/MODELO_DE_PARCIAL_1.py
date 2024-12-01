#MODELO DE PARCIAL 1: Sistema de Registro de Ventas de Entradas para el Concierto de Asspera en el Estadio River Plate.
#Se nos ha solicitado desarrollar una aplicación para llevar el registro de las entradas vendidas en el Estadio River Plate para el concierto de Asspera.
#El sistema debe solicitar al usuario la siguiente #información al momento de comprar cada entrada:
#Al comenzar el programa, se deberán ingresar los siguientes datos hasta que el usuario decida detenerse:

#Datos a Solicitar para las Ventas: (VALIDAR TODOS LOS DATOS)
#Nombre del comprador
#Edad (no menor a 16)
#Género (Masculino, Femenino, Otro)
#Tipo de entrada (General, Campo delantero, Platea)
#Medio de pago (Crédito, Efectivo, Débito)

#Lista de Precios:
#General: $16000
#Campo delantero: $25000
#Platea: $30000

#Descuentos:
#Entradas adquiridas con tarjeta de crédito: 20% de descuento sobre el precio de la entrada.
#Entradas adquiridas con tarjeta de débito: 15% de descuento sobre el precio de la entrada.

#Informes Finales: Al finalizar la carga de datos, el programa deberá mostrar los siguientes informes:
#Género más frecuente entre los compradores de entradas de tipo "Campo delantero".
#Cantidad de personas que compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
#Porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
#Total de descuentos en pesos aplicados por la empresa para pagos con tarjeta de crédito.
#Nombre y edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito (solo la primera que se encuentre).
#Cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
#Monto total recaudado por la venta de entradas de tipo "Platea" pagadas con tarjeta de débito por personas cuyas edades son múltiplos de 6.


print("\nBienvenido al sistema de ventas de River Plate, el mejor concierto de Asspera de todos los tiempos.")
print("Ingrese los datos solicitados por favor: \n")

validacion = "s"
masculino_contador = 0
femenino_contador = 0
otro_contador = 0
entrada_precio = ""
contador_personas_general = 0
contador_de_personas = 0 #Es para llevar un registro de cuantas personas compraron entradas
suma_edades = 0
promedio_edades = 0
compradores_platea = 0
contador_descuentos = 0
persona_precio_mas_alto = None
edad_persona_que_pago_mayor_precio = None
contador_edad_primo = 0
monto_total_recaudado = 0
porcentaje = ""

while True:
        # CAPTURAMOS EL NOMBRE DEL COMPRADOR Y CONVERTIMOS DESPUES EN STRING
        nombre_del_comprador = input("Nombre del comprador: ")
        
        while not nombre_del_comprador.isalpha():
            print("Nombre no válido.")
            nombre_del_comprador = input("Ingrese de nuevo el nombre: ")
        #CAPTURAMOS LA EDAD Y LA CONVERTIMOS A ENTERO CORROBORANDO QUE SEA UN NUMERO
        edad_del_comprador = input("¿Qué edad tiene? (no menor a 16): ")
        while not edad_del_comprador.isdigit() or int(edad_del_comprador) < 16:
            print("Edad no válida.")
            edad_del_comprador = input("Ingrese de nuevo la edad: ")
        edad_del_comprador = int(edad_del_comprador)  # Convertimos la edad a entero después de la validación

                
        #CAPTURAMOS EL GENERO DEL COMPRADOR
        genero_del_comprador = input("Genero: \n[1] Masculino\n[2] Femenino\n[3] Otro: \n")
        #Confirmamos que genero es el comprador mediante las validacion
        if genero_del_comprador == "1":
            genero_del_comprador = "Masculino"
        elif genero_del_comprador == "2":
            genero_del_comprador = "Femenino"
        else:
            if genero_del_comprador == "3":
                genero_del_comprador = "Otro genero"
        
        #CAPTURAMOS EL TIPO DE ENTRADA QUE QUIERE EL COMPRADOR
        entrada = input("Que entrada quiere?:\n[1] General \n[2] Campo delantero \n[3] Platea: \n")
        while not entrada.isdigit() or int(entrada) > 3 or int(entrada) < 1:
            print("Entrada no valida.")
            entrada = input("Ingrese de nuevo la entrada: ")
        entrada = int(entrada)
        
        match entrada:
            case 0:
                entrada = "General"
                entrada_precio = 16000
            case 1:
                entrada = "Campo delantero"
                entrada_precio = 12000
                match genero_del_comprador:
                    case "masculino":
                        masculino_contador += 1  
                    case "Femenino":
                        femenino_contador += 1
                    case "Otro":
                        otro_contador += 1
            case 2:
                entrada = "Platea"
                entrada_precio = 8000
                
        #CAPTURAMOS EL MEDIO DE PAGO        
        medio_de_pago = input("Medio de pago \n[1] Crédito \n[2] Efectivo \n[3] Débito: \n")
        #VALIDAMOS QUE MEDIO DE PAGO SE INGRESO
        while not medio_de_pago.isdigit() or int(medio_de_pago) < 1 or int(medio_de_pago) > 3:
            print("Medio de pago no valido.")
            medio_de_pago = input("Ingrese de nuevo el medio de pago: ")
        #Confirmamos porque medio de pago va a pagar el comprador:
        match medio_de_pago:
            case 1:
                medio_de_pago = "Credito"
                if persona_precio_mas_alto == None or entrada_precio > persona_precio_mas_alto:
                    persona_precio_mas_alto = nombre_del_comprador
                    edad_persona_que_pago_mayor_precio = edad_del_comprador
                descuento = 0.20
                #Contamos cuantos personas compraron entradas de tipo "General" pagando con tarjeta de credito para saber cuantos descuentos hay
                contador_descuentos += 1
                if entrada == "General":
                    contador_personas_general += 1
                    promedio_edades = suma_edades / contador_personas_general
            case 2:
                medio_de_pago = "Efectivo"
            case 3:
                medio_de_pago = "Debito"
                descuento = 0.15
                if entrada == "Platea":
                    compradores_platea += 1
                    #Porcentaje de personas que compraron entradas "platea" con tarjeta de crédito
                    porcentaje = (compradores_platea * 100) / contador_de_personas
                if edad_del_comprador % 1 == 0:
                    contador_edad_primo =+ 1
                #Monto total recaudado por la venta de entradas de tipo "Platea" pagadas con tarjeta de débito por personas cuyas edades son múltiplos de 6.
                if entrada == "Platea" and edad_del_comprador % 6 == 0:
                    monto_total_recaudado += entrada_precio
                
                
        validacion = input("\nDesea continuar? [S] Si - [CUALQUIER TECLA] No: ")
        if validacion != 's' and validacion != 'S':
            print("Gracias por comprar en nuestro sistema, que disfrute su concierto.\n")
            break
        contador_de_personas += 1
    
# INFORMES
#Género más frecuente entre los compradores de entradas de tipo "Campo delantero".
if masculino_contador > femenino_contador and masculino_contador > otro_contador:
    genero_mas_frecuente = "Masculino"
elif femenino_contador > masculino_contador and femenino_contador > otro_contador:
    genero_mas_frecuente = "Femenino"
else:
    genero_mas_frecuente = "Otro genero"
    
print(f"Genero mas frecuente: {genero_mas_frecuente}")

#Cantidad de personas que compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
if contador_personas_general > 0:
    print(f"La cantidad de personas que compraron entradas de tipo 'General' y pagaron con tarjeta de credito es: {contador_personas_general} y el promedio de las edades es: {promedio_edades}")
else:
    print("No hay personas que compraron entradas de tipo 'General' y pagaron con tarjeta de credito.")

#Porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
print(f"El porcentaje de personas que compraron entradas de tipo 'Platea' y pagaron con tarjeta de debito es del: {porcentaje}%")

#Total de descuentos en pesos aplicados por la empresa para pagos con tarjeta de crédito.
if contador_descuentos > 0:
    print(f"El total de descuentos aplicados por la empresa es de: {contador_descuentos * descuento} pesos")

#Nombre y edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito (solo la primera que se encuentre).
if persona_precio_mas_alto != None and edad_persona_que_pago_mayor_precio != None:
    print(f"La persona que pagó el precio mas alto por una entrada de tipo 'General' y pagó con tarjeta de debito es: {persona_precio_mas_alto} con {edad_persona_que_pago_mayor_precio} años")
else:
    print("No hay personas que hayan solicitado una entrada de tipo 'General' y pagaron con tarjeta de debito.")

#Cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
if (compradores_platea > 0) and (contador_edad_primo > 0):
    print(f"El porcentaje de personas que compraron entradas de tipo 'Platea' y cuya edad es un número primo es del: {((compradores_platea * 100) / contador_de_personas)}%")    
else:
    print("No hay personas que hayan solicitado una entrada de tipo 'Platea' y cuya edad es un número primo.")

#Monto total recaudado por la venta de entradas de tipo "Platea" pagadas con tarjeta de débito por personas cuyas edades son múltiplos de 6.
if (monto_total_recaudado > 0) and (compradores_platea > 0):
    print(f"El monto total recaudado por la venta de entradas de tipo 'Platea' pagadas con tarjeta de debito por personas cuyas edades son multiplos de 6 es de: {monto_total_recaudado} pesos")
else:
    print("No hay personas que hayan solicitado una entrada de tipo 'Platea' y pagaron con tarjeta de debito.")

