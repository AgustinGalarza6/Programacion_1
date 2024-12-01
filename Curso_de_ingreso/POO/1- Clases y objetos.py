# Las clases en python se definen con pascalCase (todas las primeras letras de la palabra seran mayusculas)
# por ejemplo: class Celulares o class NombreDeCelular

class NombreDelCelular():
    marca = "Samsung"
    modelo = "S23 ULTRA"
    camara = "48MP"
# ESO SERIA CREAR UNA CLASE (NO ES UN OBJETO)

celular = NombreDelCelular()

#Por ejemplo si queremos consultar algo sobre la clase del objeto: (¿Que marca es?)
print(NombreDelCelular.marca)

