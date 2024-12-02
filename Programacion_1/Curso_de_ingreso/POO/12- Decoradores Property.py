# property = propiedades
# las propiedades son setters y getters pero con algo mas: los deleters



# class Persona():
#     def __init__ (self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad

#     def get_nombre(self):
#         return self._nombre
    
# Agustin = Persona("Agustin", 23)

# nombre = Agustin.get_nombre()
# print(nombre)



# Apliquemos Property a esas lineas de codigo 

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property #Con property indicamos que es un getter, y por otro lado por medio de el podemos renombrar la funcion y ocultar el verdadero nombre del atributo privado "__nombre"
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @nombre.deleter #Con el deleter podemos borrar el atributo
    def nombre(self):
        del self._nombre

# Crear una instancia de Persona
agustin = Persona("Agustin", 23)

# Usar el getter para obtener el nombre
print(agustin.nombre)

# Usar el setter para cambiar el nombre
agustin.nombre = "Agustin Galarza"
print(agustin.nombre)

#Despues que se ejecutan y aplicamos un DEL ahora, y no existe mas el atributo nombre
#Si despues se quisiera printear de nuevo el nombre, ya no se podria y da error xq fue eliminado.

del agustin.nombre
print(agustin.nombre) # daria error, no existe el atributo.

# Agustin (Se ejecuta el primer nombre)
# Agustin Galarza (Se ejecuta el nuevo nombre con el setter)

#aca es donde entra el deleter

# Y si se quiere printear de nuevo el nombre salta error:
# Traceback (most recent call last):
#   File "c:\UTN\Curso_de_ingreso\POO\12- Decoradores Property.py", line 54, in <module>
#     print(agustin.nombre) # daria error, no existe el atributo.
#           ^^^^^^^^^^^^^^
#   File "c:\UTN\Curso_de_ingreso\POO\12- Decoradores Property.py", line 30, in nombre
#     return self._nombre
#            ^^^^^^^^^^^^
# AttributeError: 'Persona' object has no attribute '_nombre'. Did you mean: 'nombre'?
# PS C:\UTN> 