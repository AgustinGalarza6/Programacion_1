# Nos encargan el desarrollo de una aplicacion que le permite a sus usuarios operar en la bolsa de valores:
# de los inversionistas, no se sabe cuantos, registrar:
# 1- Nombre
# 2- Monto en pesos de la operacion (no menor a 10000)
# 3- Cantidad de instrumentos --- Tipo: (CEDEAR, BONOS, MEP)

contador_tipo_instrumento_cedear = 0
contador_tipo_instrumento_bonos = 0
contador_tipo_instrumento_mep = 0
intrumento_mas_operado = None
cantidad_usuarios_entre_150_y_200 = 0
validacion = 's'
contador_inversionistas_mep = 0
contador_de_usuarios = 0

while True:
        nombre = input('Dame un nombre: ')
        #Validamos que el nombre no este vacio
        while len(nombre) == 0:
            print('[ERROR] EL NOMBRE ESTA VACIO')
            nombre = input('Dame un nombre nuevamente: ')
        
        #Solicitamos monto
        monto = input('Dame un monto: ')
        #Validamos que el monto no sea menor a 10000
        while len(monto) == 0 and int(monto) < 10000:
            print('[ERROR] EL MONTO ES MENOR A 10000')
            monto = input('Dame un monto nuevamente: ')
        monto = int(monto)
        
        #Cantidad de instrumentos (Representan una participación en la propiedad de una empresa o entidad.)
        instrumentos = input('Dame la cantidad de instrumentos: ')
        #Validamos que el tipo no este vacio
        while len(instrumentos) == 0:
            print('[ERROR] LA CANTIDAD DE INSTRUMENTOS ESTA VACIA')
            instrumentos = input('Dame la cantidad de instrumentos nuevamente: ')
        
        #Solicitamos tipo de instrumento
        tipo_de_instrumento = input('Seleccione el tipo de instrumento:\n[1] CEDEAR \n[2] BONOS \n[3] MEP\nSeleccione una opcion: ')
        #Validamos que el tipo no este vacio
        while len(tipo_de_instrumento) == 0:
            print('[ERROR] EL TIPO DE INSTRUMENTO ESTA VACIO')
            tipo = input('Dame un tipo de instrumento nuevamente: ')
        if tipo_de_instrumento == '1':
            contador_tipo_instrumento_cedear += 1
        elif tipo_de_instrumento == '2':
            contador_tipo_instrumento_bonos += 1
            if (monto >= 150 and monto <= 200) and (monto >= 50000):
                cantidad_usuarios_entre_150_y_200 += 1     
        elif tipo_de_instrumento == '3':
            contador_tipo_instrumento_mep += 1
            if (monto > 20000 and monto < 50000):
                contador_inversionistas_mep += 1
        else:
            print('[ERROR] OPCION INVALIDA')
            tipo_de_instrumento = input('Dame un tipo de instrumento nuevamente: ')
            
        contador_de_usuarios =+ 1
        
        validacion = input("\nDesea continuar? [S] Si - [CUALQUIER TECLA] No: ")
        if validacion != 's' and validacion != 'S':
            print("Chau!\n")
            break
        

# INFORMAR
# 1- Tipo de instrumento que mas se opero 
if (contador_tipo_instrumento_cedear > contador_tipo_instrumento_bonos) and (contador_tipo_instrumento_cedear > contador_tipo_instrumento_mep):
    print('El tipo de instrumento que mas se opero es: CEDEAR')
elif (contador_tipo_instrumento_bonos > contador_tipo_instrumento_cedear) and (contador_tipo_instrumento_bonos > contador_tipo_instrumento_mep):
    print('El tipo de instrumento que mas se opero es: BONOS')
elif (contador_tipo_instrumento_mep > contador_tipo_instrumento_bonos) and (contador_tipo_instrumento_mep > contador_tipo_instrumento_cedear):
    print('El tipo de instrumento que mas se opero es: MEP')

# 2- Cantidad de usuarios que compraron entre 150 y 200 BONOS y que hayan invertido mas de $50000
if cantidad_usuarios_entre_150_y_200 > 0:
    print('La cantidad de usuarios que compraron entre 150 y 200 BONOS y que hayan invertido mas de $50000 es de: ', cantidad_usuarios_entre_150_y_200)
else:
    print('No hay usuarios que compraron entre 150 y 200 BONOS y que hayan invertido mas de $50000')

# 3- Nombre y cantidad de instrumentos del usuario que compro BONOS o MEP, que menos dinero invirtio


# 4- Porcentaje de USUARIOS que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000     
if contador_inversionistas_mep > 0:
    print('El porcentaje de USUARIOS que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000 es de: ', (contador_inversionistas_mep*100)/contador_de_usuarios)
else:
    print('No hay USUARIOS que invirtieron en MEP, cuyo monto se encuentre entre $20000 y $50000')