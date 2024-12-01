# El encapsulamiento es el public y el private de otros lenguajes.
# Es una forma de ocultar la informacion de la clase.

# En python el encapsulamiento pueden ser de 3 maneras diferentes:

# Publico: se puede acceder desde cualquiera.
# Protegido: solo se puede acceder desde la clase o la subclase. Se expresan con "_"
# Privado: solo se puede acceder desde la clase. Se expresan con "__" (doble subrayado)


# Ejemplo:
class Miclase():
    def __init__(self):
        self.__privado = "Esto es privado" # Atributo privado "__"
        self._protegido = "Esto esta protegido." # Atributo protegido "_"
        self.publico = "Esto es publico" # Atributo publico

