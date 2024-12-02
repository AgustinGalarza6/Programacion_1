class Persona(): #ESTA ES NUESTRA CLASE PADRE
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

class Empleado(Persona): #ESTA ES NUESTRA CLASE HIJA QUE HEREDA LAS PROPIEDADES DE LA CLASE PADRE (PERSONA)
    # pass: CON PASS CREAMOS ALGO PERO NO QUEREMOS DEFINIR QUE VA A HACER.
    def __init__(self, nombre, edad, nacionalidad, sueldo, trabajo):
        #CON SUPER APLIACAMOS LA HERENCIA DE PERSONA Y AGREGAMOS APARTE SUELDO Y TRABAJO, PERO SOLO DE LA CLASE HIJA
        #EN LA CLASE PADRE (PERSONA) SUELDO Y TRABAJO NO EXISTE.
        super().__init__(nombre, edad, nacionalidad)
        self.sueldo = sueldo
        self.trabajo = trabajo
    def trabajar(self):
        print(f"Yo trabajo como {self.trabajo}")

Roberto = Empleado("Roberto", 32, "Argentino", 5000, "Programador")
# Llamamos a los metodos
# Roberto oomo Heredo el metodo SALUDAR de persona que es nuestra clase padre
# el tambien puede saludar. Sin importar que el metodo saludar no este dentro
# de la clase empleado.

#Tambien el metodo saludar puede ser modificado dentro de empleado y solo se modifica
# en la clase hija.

# Otro dato interesante tambien es que 
Roberto.saludar()
Roberto.trabajar()