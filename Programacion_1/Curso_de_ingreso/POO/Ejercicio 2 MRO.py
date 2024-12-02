class Animal:
    def Comer(self):
        print("Estoy comiendo")

class Mamifero:
    def Amamantar(self):
        print("Estoy amamantando")

class Ave:
    def Volar(self):
        print("Estoy volando")

class Murcielago(Animal, Mamifero, Ave):
    pass

#Creamos un murcielago
murcielago = Murcielago()

#Llamamos a los metodos
murcielago.Amamantar()
murcielago.Comer()
murcielago.Volar()