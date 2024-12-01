def calcular_edad(dia_nac, mes_nac, ano_nac, dia_act, mes_act, ano_act):
    '''
    En esta funcion lo que vamos a hacer es solicitar los datos necesarios sobre en que fecha nacio
    el usuario y en que fecha actual se encuentra de manera individual.

        Logrando asi que por medio de un pedido invidual para cada cosa podamos parcear de STR a INT.

        La funcion de calculo_edad se encarga de tomar los datos del año actual y de nacimiento ya parceados
        para poder hacer el calculo y nos returne por resultado final que edad tiene nuestro usuario.
    '''
    edad = ano_act - ano_nac
    return edad

# Solicitar datos de nacimiento
dia_de_nacimiento = int(input('Ingrese en qué día nació (En números): '))
mes_de_nacimiento = int(input('Ingrese en qué mes nació (En números): '))
año_de_nacimiento = int(input('Ingrese en qué año nació (En números): '))

# Solicitar datos actuales
dia_actual = int(input('Ingrese qué fecha es hoy (En números): '))
mes_actual = int(input('Ingrese qué mes es (En números): '))
año_actual = int(input('Ingrese el año actual (En números): '))

# Calcular y mostrar la edad
edad = calcular_edad(dia_de_nacimiento, mes_de_nacimiento, año_de_nacimiento, dia_actual, mes_actual, año_actual)
print(f"\nLa edad del usuario es {edad} años")