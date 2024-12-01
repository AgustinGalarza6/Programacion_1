# 2) Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
# letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
# respectivamente.

def extraer_string(cadena:str, desde:int, hasta:int) -> str:
    contador = 1
    resultado = ""
    for letra in cadena:
        if contador >= desde and contador <= hasta:
            resultado += letra 
        contador += 1
    
    return resultado

def mostrar_vehiculo(patente:str) -> str:
    '''
    funcion que recibe una patente como parametro 
    retorna tipo de vehiculo
    '''
    letra1 = extraer_string(patente, 1, 1)
    
    if ord(letra1) > 47 and ord(letra1) < 58:
        vehiculo = "Moto"
    else:
        vehiculo = "Auto"

    return vehiculo

print(mostrar_vehiculo("192 AFG"))
print(mostrar_vehiculo("AFG 192"))
print("\n")
print("\n")
# ABC 123
# 123 ABC