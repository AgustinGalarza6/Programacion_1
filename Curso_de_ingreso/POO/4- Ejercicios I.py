class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    #Metodos
    def estudiar(self):
        print(f"{self.nombre} esta estudiando.")

# Pedimos los atributos
nombre = input("Ingresa el nombre del estudiante: ")
edad = int(input("Ingresa la edad del estudiante: "))
grado = input("Ingresa el grado del estudiante: ")

# Guardamos los atributos en un objeto
estudiante = Estudiante(nombre, edad, grado)

# Mostramos los datos en pantalla:

print(f"""
Datos del estudiante: \n
El estudiante se llama: {estudiante.nombre}\n
El estudiante tiene: {estudiante.edad} años\n
Y el estudiante esta en el grado: {estudiante.grado}\n
""")

# Llamamos al metodo
while True:
    estudiar = input("¿Estas estudiando?: ")
    if (estudiar.lower() == "si"):
        estudiante.estudiar()
        break
    else:
        print(f"{estudiante.nombre} no esta estudiando.")
        break

