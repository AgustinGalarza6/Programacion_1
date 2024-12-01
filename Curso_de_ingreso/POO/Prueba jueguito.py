class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.esta_vivo = True

    def atacar(self, objetivo):
        if self.esta_vivo:
            objetivo.vida -= self.ataque

    def morir(self):
        self.esta_vivo = False
    
class Enemigo(Personaje):
    def __init__(self, nombre, vida, ataque):
        super().__init__(nombre, vida, ataque)

    def atacar(self, objetivo):
        if self.esta_vivo:
            super().atacar(objetivo)

    def morir(self):
        super().morir()

# Crear un enemigo
enemigo = Enemigo("Boss", 100, 15)

# Crear un personaje
personaje = Personaje("Kratos", 100, 20)


personaje.atacar(enemigo)
print(f"Ataque del personaje: -{personaje.ataque} de vida") # -20
print(f"Vida restante del enemigo: {enemigo.vida}") # 80 de vida restante

enemigo.atacar(personaje)
print(f"\nAtaque del enemigo: -15 de vida") # -15 de vida
print(f"Vida restante del personaje: {personaje.vida}") # 85 de vida restante

personaje.atacar(enemigo)
print(f"\nAtaque del personaje: -{personaje.ataque} de vida") # -20
print(f"Vida restante del enemigo: {enemigo.vida}") # 60 de vida restante

enemigo.atacar(personaje)
print(f"\nAtaque del enemigo: -15 de vida") # -15 de vida
print(f"Vida restante del personaje: {personaje.vida}") # 70 de vida restante

personaje.atacar(enemigo)
print(f"\nAtaque del personaje: -{personaje.ataque} de vida") # -20
print(f"Vida restante del enemigo: {enemigo.vida}") # 40 de vida restante

enemigo.atacar(personaje)
print(f"\nAtaque del enemigo: -15 de vida") # -15 de vida
print(f"Vida restante del personaje: {personaje.vida}") # 55 de vida restante

personaje.atacar(enemigo)
print(f"\nAtaque del personaje: -{personaje.ataque} de vida") # -20
print(f"Vida restante del enemigo: {enemigo.vida}") # 20 de vida restante

enemigo.atacar(personaje)
print(f"\nAtaque del enemigo: -15 de vida") # -15 de vida
print(f"Vida restante del personaje: {personaje.vida}") # 40 de vida restante

personaje.atacar(enemigo)
print(f"\nAtaque del personaje: -{personaje.ataque} de vida") # -20
print(f"Vida restante del enemigo: {enemigo.vida}") # 0 de vida restante


# Verificar si el personaje le queda vida...
if enemigo.vida == 0:
    print(f"\nEl {enemigo.nombre} ha sido derrotado")

if personaje.vida == 0:
    print(f"El personaje {personaje.nombre} ha sido derrotado")