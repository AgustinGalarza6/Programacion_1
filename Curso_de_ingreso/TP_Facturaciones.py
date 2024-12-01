#Para el departamento de facturación:
#A. Ingresar tres precios de productos y mostrar la suma de los mismos.

print("Departamento A")
precio_1 = float(input("Ingresa el primer precio: "))
precio_2 = float(input("Ingresa el segundo precio: "))
precio_3 = float(input("Ingresa el tercer precio: "))

Total_de_los_precios = (precio_1 + precio_2 + precio_3)
print("EL total es de los productos es: ",Total_de_los_precios)


#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.

print("Departamento B")
precio_1 = float(input("Ingresa el primer precio: "))
precio_2 = float(input("Ingresa el segundo precio: "))
precio_3 = float(input("Ingresa el tercer precio: "))

promedio_de_los_precios = (precio_1 + precio_2 + precio_3) / 3
print("El promedio de los productos es: ",promedio_de_los_precios)


#C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

print("Departamento C")
precio_1 = float(input("Ingresa el primer precio: "))
precio_2 = float(input("Ingresa el segundo precio: "))
precio_3 = float(input("Ingresa el tercer precio: "))

precio_final_mas_IVA = (precio_1 + precio_2 + precio_3) * 1.21
print("El precio final de los productos + IVA es: ", precio_final_mas_IVA)