# Clase -> Molde / Receta

# Objeto -> Instancia de la clase

# Clase str
# objeto "Hola mundo" (instancia de la clase str)
# saludo = "Hola mundo"
# despido = "chau"
# mi_lista = ["A", "B", "C"]

class Persona:   # UpperCamelCase   =!=  snake_case
    # Atributos (caracteristicas): altura, peso, nombre, apellido, edad, DNI, genero.
    # self.nombre, self.apellido, etc
    # Constructor
    def __init__(self, altura:int, peso:int, nombre:str, apellido:str, edad:int, documento_unico:int, fecha_nac:str, genero:str="M"):
        self.fecha_nac = fecha_nac
        self.altura = altura  # Publico
        self._peso = peso 
        self.__nombre = nombre # Privado
        self.apellido = apellido
        self.edad = edad
        self.DNI = documento_unico
        self.estado_activo = True
        self.genero = genero

    # Getters y Setters

    # Metodos (comportamientos):
    def mostrar_nombre(self): # Getter
        return self.__nombre
    
    def modificar_nombre(self, nombre:str): # Setter
        # Validan el dato que recibe por parametro
        self.__nombre = nombre
    
    def get_edad(self):
        self.fecha_nac = 22222
        # Fecha de hoy
        # Logica que calcula la edad
        # return edad

    def presentarase(self):
        print(f"Hola, mi nombre es {self.__nombre} y tengo {self.edad} años")


#######################################################################

persona_a = Persona(180, 90, "Val", "Pavlov", 35, 12345678, "16/05/1990")  
persona_b = Persona(160, 80, "Sofia", "Perez", 40, 87654321, "28/07/1995", "F")

persona_a.presentarase()