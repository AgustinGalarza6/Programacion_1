nombre = None
altura = None
altura_minima = None
el_nombre_mas_bajito = None
flag_altura_primer_ingreso = True


nombre = input('')
while nombre == '':
    nombre = input('')


altura = input('')
while altura > 100:
    altura = input('')

if altura_minima == None or altura < altura_minima:
    altura_minima = altura
    el_nombre_mas_bajito = nombre





cantidad_jugadores_rango_bajas = 0
edad = input('') 
muertes = input('') 
# E) Cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas están entre 10 y 15
if (edad >= 20 and edad <= 30) and (muertes >= 10 and muertes <= 15):
    cantidad_jugadores_rango_bajas += 1