# En python todas las variables son objetos.
# El lenguaje compilado traduce las secuenias
# Los lenguajes interpretados como python por ejemplo, traduce el lenguaje en el momento a binario y se lo envia a la computadora.

# Cada lenguaje tiene una syntax diferente

# Python es orientado a inteligerncia artificial por motivos de interprete
# C que es compilado, se aplica a procesos mas pesados, ya que al interpretarlo antes de usarlo tiene mejor rendimiento a la hora de ejecutarlo

# Todas las variables en python tienen "un valor, un tipe y un ID unico".
# Python cuando tiene 2 variables con el mismo valor, comparte el mismo ID

'''
Por ejemplo si tengo:
numero_a = 10
numero_b = 10

Los ID de numero_a y numero_b es el mismo.
'''

# Todos los examenes se deben defender, hay que tener claro por ejemplo los tipos de datos de las variables.

# NOT IN es un iterador.


'''
Ejemplo de CASTING

numero_a = 3.70

numero_b_int = int(numero_a)
print(numero_b_int)
'''

# Se usa match cuando tenes muchos casos y se busca una igualdad.
# Match no aplica para buscar rangos

# En el match el or es "| (pipe)"
'''
Ejemplo
match numero_b_int:
    case 3.70 | 3.6
        print("Numero flotante")
'''

# Investigar sobre PEP (https://peps.python.org/pep-0008/)
# RANGE FUNCIONA COMO UNA FUNCION PERO NO ES UNA FUNCION ES UNA CLASE
# RANGE GENERA UN OBJ ITERABLE (https://docs.python.org/3/library/functions.html#range)
'''
POR EJEMPLO range(3) = [0, 1, 2] (objeto iterable)

mi_rango = range(5) # Genera un objeto iterable [0, 1, 2, 3, 4]

Entonces podemos ingresar de las distintas 2 maneras:

for i in range (0, 5)
o
for i in range(5)

'''

# Si queremos por ejemplo usar for pero para listas no usamos range
'''
En este caso seria:
lista = [Agustin, Marta, Carlos]

for nombre in lista:
    print (nombre)
'''

# range(desde, hasta, pasos)

# un for puede recorrer cualquier objeto iterable
# ejemplo de iteracion de string

'''
saludo = "hola mundo"

for letra in saludo:
    print(letra)
'''

# ejemplo de for en otro for
# con el primer for recorremos las letras y por cada letra tenemos otro for que recorre los numeros
'''
letras = "ABCD"
numeros = "1234"

for letra in letras:
    for numero in numeros:
        print(letra, numero) imprime 16 resultados (4x4)
'''

