class Persona():
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Definimos el metodo:
    def ImprimirNombreYEdad(self):
        print(f"El nombre del estudiante es: {self.nombre} y su edad es {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) # Cuando usamos super para heredar, no se usa self en el parentesis.
        self.grado = grado

    def ImprimirGrado(self):
        print(f"El año de universidad actual del estudiante es: {self.grado}")



#Creamos la instancia:
Estudiante1 = Estudiante("Agustin", 23, "Primer Año")

#Llamamos al metodo:
Estudiante1.ImprimirNombreYEdad()
Estudiante1.ImprimirGrado()