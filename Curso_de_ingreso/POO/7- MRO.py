"""
¿Que es el MRO? 
El MRO viene de la frase method resolution order (orden de resolución de métodos).
A la hora de llamar a metodos de distintas clases padres, va a traer el metodo que corresponda segun el 
orden de jerarquia.

Pensemos que si tengo 10 clases con el mismo metodo, python va a tomar el metodo de la clase padre
que este primero respecto al orden de jerarquia. (MRO)
"""

class A:
    def saludo(self):
        print("hola desde A")

class B(A):
    def saludo(self):
        print("hola desde B")

class C(A):
    def saludo(self):
        print("hola desde C")

"""
class D(B, C):
    def saludo(self):
        print("hola desde D")

d = D()
d.saludo()

En este caso como D tiene definido su metodo saludo(), primero va a buscar en D e imprimir Hola desde D.
"""



"""
Ahora si tenemos el mismo ejemplo, pero SIN definir el metodo saludo() dentro de D.
En este caso primero va a buscar en B e imprimir Hola desde B.
Porque? Por el orden o MRO. B esta primero que C. Entonces primero python va a tender a buscar
en B y en despues en C.

class D(B, C):
    pass

d = D()
d.saludo()

"""

"""
# Ahora si tenemos el mismo caso pero B en vez de tener el metodo, tiene pass

class B(A):
    pass

class C(A):
    def saludo(self):
        print("hola desde C")

class D(B, C):
    pass

d = D()
d.saludo()
# Esto imprime "Hola desde C" porque pasa de B a C.

"""

"""
Y si tenemos en todas pass?

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.saludo()
Esto imprime "Hola desde A" porque buscaria en la clase que heredo B y C.
Y en si, la clase padre de todas las clases

"""