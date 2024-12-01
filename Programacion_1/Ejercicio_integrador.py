# Ejercicio Integrador 01
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:

# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.


# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.


barbijo_mas_caro = None
barbijo_mas_caro_unidades = None
barbijo_mas_caro_fabricante = None
item_mas_unidades = None
item_mas_unidades_fabricante = None
cantidad_jabones = 0

print("Bienvenidos al sistema de división de higiene")

for i in range(5):
    tipo = input("Tipo: ")
    while tipo != "barbijo" and tipo != "jabón" and tipo != "alcohol":
        tipo = input("Tipo: ")

    precio = int(input("Precio: "))
    while precio < 100 or precio > 300:
        precio = int(input("Precio: "))

    cantidad = int(input("Cantidad: "))
    while cantidad <= 0 or cantidad > 1000:
        cantidad = int(input("Cantidad: "))

    marca = input("Marca: ")

    fabricante = input("Fabricante: ")

    # LOGICA #A. 
    if barbijo_mas_caro == None or precio > barbijo_mas_caro:
        barbijo_mas_caro = precio
        barbijo_mas_caro_unidades = cantidad
        barbijo_mas_caro_fabricante = fabricante

    # LOGICA #B.
    if item_mas_unidades == None or cantidad > item_mas_unidades:
        item_mas_unidades = cantidad
        item_mas_unidades_fabricante = fabricante

    # LOGICA #C.
    if tipo == "jabón":
        cantidad_jabones += cantidad


# INFORMES

# A
if barbijo_mas_caro is None:
    print("No se ingresaron barbijos.")
else:
    print(f"El barbijo más caro cuesta: {barbijo_mas_caro}, la cantidad de unidades es de: {barbijo_mas_caro_unidades} y es fabricado por: {barbijo_mas_caro_fabricante}")

# B
if item_mas_unidades is None:
    print("No se ingresaron ítems.")
else:
    print(f"El ítem con más unidades tiene: {item_mas_unidades} unidades, fabricado por: {item_mas_unidades_fabricante}")

# C
if cantidad_jabones is 0:
    print("No se ingresaron jabones.")
else:
    print(f"La cantidad total de jabones es de: {cantidad_jabones} unidades")