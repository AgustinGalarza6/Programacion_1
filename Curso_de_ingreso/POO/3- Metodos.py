# Un metodo no es mas que una funcion
class Celular():
    # METODO CONSTRUCTOR (ESPECIAL)
    def __init__(self, marca, modelo, camara):
        # PROPIEDADES DEL OBJETO
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    # METODOS O ACCIONES QUE QUIERAS QUE HAGA TU OBJETO
    def llamar(self):
        print(f"Estoy llamando desde mi: {self.modelo}")

    def tomar_foto(self):
        print(f"Estoy tomando una foto desde mi: {self.modelo}")

celular_1 = Celular("Samsung", "S23 ULTRA", "48MP")
celular_2 = Celular("Apple", "Iphone 13", "30MP")

print(celular_1.llamar())