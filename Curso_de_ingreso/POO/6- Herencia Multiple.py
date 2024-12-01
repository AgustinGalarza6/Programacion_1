class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

# HERENCIA MULTIPLE: CREAMOS UNA CLASE LLAMADA ARTISTA PARA VER EL CONCEPTO
class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
    def presentarse(self):
        print(f"Hola, soy {self.habilidad}")

class EmpleadoArtista(Persona, Artista): 
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    # Llamamos a un metodo anterior de la clase Artista
    def presentarse(self):
        return f"{super().presentarse()}" 
        #En terminos generales, con SUPER llamamos
        #al metodo de la clase padre. Con self, llamamos a metodos de la clase especifica en la que estamos.