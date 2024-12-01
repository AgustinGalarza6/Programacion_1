# Opcion 1:
import PPT_funciones
print(PPT_funciones.extraer_string("Hola mundo", 1, 5))

# Opcion 2:
from PPT_funciones import extraer_string
print(extraer_string("Hola mundo", 1, 5))

# Opcion 3:
from PPT_funciones import *
print(extraer_string("Hola mundo", 1, 5))