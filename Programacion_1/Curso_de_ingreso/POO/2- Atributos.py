"""
# Los atributos son variables que pertenecen a una clase predefinida
class NombreDelCelular():
    marca = "Samsung"
    modelo = "S23 ULTRA"
    camara = "48MP"

# Aca tenemos nuestro objeto (Celular)
celular = NombreDelCelular()
# Y aca nuestro atributo es: Marca
# Dentro de la clase NombreDelCelular hay una variable llamada "marca" que es un atributo.
print(NombreDelCelular.marca)

"""


# Ejercicio Fabrica de celulares

#Creamos la clase y seguido de eso el constructor (FUNCION CONSTRUCTORA (DEF) )
class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular_1 = Celular("Samsung", "S23 ULTRA", "48MP")
celular_2 = Celular("Apple", "Iphone 13", "30MP")


print(celular_2.modelo)
