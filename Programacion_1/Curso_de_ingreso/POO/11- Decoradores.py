# Ejemplo de decorador
def decorador(funcion):
    def nueva_funcion():
        print("Mandame a llamar a este pibe...")
        funcion()
        print("Como andas rey?")
    return nueva_funcion

# def saludo():
#     print("Hola amigazo!")

# saludo = decorador(saludo)
# saludo()
# Estos 2 renglones se reemplazan por un simple "@decorador"

# Como aplicamos lo de aca arriba con un decorador? (como se deberia de hacer en si)
@decorador
def saludo():
    print("Hola amigazo!")

saludo()

# los decoradores son funciones que agarran una funcion como parametro y retornan una nueva funcion (le agrega algo extra)
# La funcion original no se modifica, solo agraga funcionalidades antes o despues de la original, o ambas.