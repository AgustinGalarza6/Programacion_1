# Los setters y los getters son propiedades que nos permiten acceder y modificar los atributos de una clase privada.
class Persona():
    def __init__ (self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    #Aplicamos un getter (Una funcion que accede al nombre protegido de la clase)
    def get_nombre(self):
        return self._nombre
    
    # Creamos un set (una funcion que modifica el nombre protegido de la clase)
    def set_nombre(self, New_Nombre):
        self._nombre = New_Nombre

Agustin = Persona("Agustin", 23)

#Accedemos al atributo protegido por medio de un getter
nombre = Agustin.get_nombre()
print(nombre)

# Modificamos el nombre con un setter 
Agustin.set_nombre("/set  Nuevo nombre: Agustin Galarza")

nombre = Agustin.get_nombre()
print(nombre)


# Los getters en terminos generales son funciones que nos permiten acceder a los atributos de una clase privada.
# En este ejemplo creamos un getter para acceder al atributo protegido NOMBRE de la clase persona