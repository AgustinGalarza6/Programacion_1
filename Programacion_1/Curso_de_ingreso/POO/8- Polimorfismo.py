"""
Polimorfismo es cuando una varias clases tienen los mismos metodos pero cada uno de ellos se comportan de diferente manera
Por ejemplo:
"""

class Perro():
    def sonido(self):
        return "Estoy ladrando"

class Gato():
    def sonido(self):
        return "Estoy maullando"
    
Gato = Gato()
Perro = Perro()

print(Perro.sonido())
print(Gato.sonido())

"""
Como vemos en este ejemplo, aplicamos polimorfismo respecto a los sonidos dependiendo el tipo de animal.
El gato cuando hace sonido maulla y el perro ladra. Cumpliendo asi el polimorfismo, igual metodo, diferente comportamiento.
"""