# Una función recursiva en Python es una función que se llama a sí misma dentro de su propio cuerpo para resolver un problema.
# Este tipo de funciones es útil para problemas que se pueden dividir en subproblemas más pequeños y similares al problema original.
# La recursión permite que una tarea compleja se divida en pasos más manejables.

# Una función recursiva debe tener dos componentes clave:
# Caso base: Es la condición que detiene la recursión. Sin un caso base, la función continuaría llamándose a sí misma indefinidamente, lo que podría llevar a un desbordamiento de pila (stack overflow).
# Llamada recursiva: Es la parte de la función en la que se llama a sí misma con un argumento diferente, generalmente más simple o reducido, acercándose al caso base.


def factorial(n):
    # Caso base: si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva: n multiplicado por el factorial de n-1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
print(factorial(5))  # Salida: 120


# En este ejemplo:

# El caso base es cuando n es 0 o 1, en cuyo caso la función devuelve 1.

# La llamada recursiva es n * factorial(n - 1), que reduce el problema hasta que se alcanza el caso base.


# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Una funcion recursiva es una funcion que se llama a si misma.
# Generalmente son funciones las cuales mientras se llaman a si mismas, por lo general siempre resuelven el mismo problema repetidamente.

# Si una funcion recursiva no tiene una condicion de break, se ejecuta hasta que salte un error por falta de memoria


# Ejemplo:
def calcular_factorial(numero:int)->int:
    if numero == 0:
        Factorial = 1
    else:
        Factorial =  numero * calcular_factorial(numero - 1)
    return Factorial

print(calcular_factorial(5))

# 1) Desarrollar función calcular_fibonacci.
# Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
# Funcionalidad: La función deberá calcular el número n-ésimo en la sucesión de Fibonacci.
# Si n = 0, deberá devolver 0.
# Si n = 1, deberá devolver 1.
# Para cualquier n > 1, el resultado será la suma de los dos números anteriores de la secuencia.
# Retorno: El resultado calculado previamente.
# Por ejemplo:
# ● f 0 = 0
# ● f 1 = 1
# ● f 2 = 1
# ● f 3 = 2
# ● f 4 = 3
# ● f 5 = 5
# ● f 6 = 8

def calcular_fibonacci(numero:int)->int:
    if numero < 2:
        resultado = numero
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    return resultado
print(calcular_fibonacci(7))

# 2) Desarrollar función mostrar_serie_fibonacci.
# Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
# Funcionalidad: La función deberá mostrar la secuencia completa hasta el número n-ésimo en la sucesión de
# Fibonacci, incluyendo a este último.
# Retorno: None

def mostrar_serie_fibonacci(numero:int)->None:
    for i in range(0, numero + 1):
        print(f"● f {i} = {calcular_fibonacci(i)}")
    return None

mostrar_serie_fibonacci(7)

