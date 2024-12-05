import random

"""
1) Diseñar un algoritmo que utilice dos variables una a y b calcule la suma, resta, multiplicación y división,
en la sentencias de salida que tengan este formato ejemplo: 3+4=7. Realizar la prueba de escritorio
para a=27 y b=-5.

"""

a = 30
b = 10

print(f'{a} + {b}= {a+b}')
print(f'{a} - {b}= {a-b}')
print(f'{a} * {b}= {a*b}')
print(f'{a} / {b}= {a/b}')

#----------------------------------------------------------------------------------------------------------------------------------------------

"""
2) Diseñar un algoritmo que dado el radio de un círculo calcule el área y la longitud de circunferencia.
Realizar la prueba de escritorio para r=3.

"""

r = 3

area = 3.14 * r * r
longitud = 2 * 3.14 * r

print(f'\nEl area del circulo es: {area:.1f}')
print(f'La longitud del circulo es: {longitud:.1f}')

#----------------------------------------------------------------------------------------------------------------------------------------------

"""
3) Diseñar un algoritmo que dados los catetos de un triángulo rectángulo, calcule la hipotenusa, el área y
el perímetro. Realizar la prueba de escritorio para catetoMenor = 3 y catetoMayor=5.

"""

catetoMenor = 3
catetoMayor = 5

hipotenusa = (catetoMenor ** 2 + catetoMayor ** 2) ** 0.5
area = (catetoMenor * catetoMayor) / 2
perimetro = catetoMenor + catetoMayor + hipotenusa

print(f'\nLa hipotenusa del triangulo rectangulo es: {hipotenusa:.1f}')
print(f'El area del triangulo rectangulo es: {area:.1f}')
print(f'El perimetro del triangulo rectangulo es: {perimetro:.1f}')

#----------------------------------------------------------------------------------------------------------------------------------------------

"""
4) Diseñar un algoritmo que lea dos variables lógicas p y q. Calcule en tres variables NO p, NO q, p Y q y
p O q y por último muestre los resultados. Realizar la prueba de escritorio para los Escenario 1: p=V,
q=V; Escenario 2: p=V, q=F; Escenario 3: p=F, q=V; Escenario 4: p=F, q=F;

"""

p = False 
q = True 

no_p = not p 
no_q = not q 
p_y_q = p and q 
p_o_q = p or q

print(f'\nNo p: {no_p}')
print(f'No q: {no_q}')
print(f'p y q: {p_y_q}')
print(f'p o q: {p_o_q}')

#----------------------------------------------------------------------------------------------------------------------------------------------

"""
5) Diseñar un algoritmo que dados dos números cualquiera, calcule el resto de la división entre ambos,
finalmente imprima los números dados y el resultado. Realizar la prueba de escritorio con los siguientes
valores de lectura: dividendo=39 y divisor=11.

"""
dividendo = 39
divisor = 11

resto = dividendo % divisor

print(f'\nEl dividendo es: {dividendo}')
print(f'El divisor es: {divisor}')
print(f'El resto de la division es: {resto}') # resto 6

#----------------------------------------------------------------------------------------------------------------------------------------------

"""
6) Diseñar un algoritmo para simular tirar dos dados y sumar las dos caras resultantes. Mostrar los
números que salieron y su suma. Realizar la prueba de escritorio suponiendo que el 1° dado arroja un
5 y el segundo un 6.

"""

dado_1 = random.randint(1,6)
dado_2 = random.randint(1,6)

suma_de_dados = dado_1 + dado_2

print(f'\nDado 1: {dado_1}')
print(f'Dado 2: {dado_2}')
print(f'Total: {suma_de_dados}')

#----------------------------------------------------------------------------------------------------------------------------------------------

