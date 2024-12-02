# Def variables
precio_de_las_lamparas = int(800)
cant_de_lamparas = int(input("Cuantas lamparas quiere?: "))
Subtotal = cant_de_lamparas * precio_de_las_lamparas
descuento = Subtotal * 0.5 # Osea el subtotal * 0.5 que seria su %50
total_a_pagar = Subtotal - descuento
marca_de_lampara = input("Que marca va a llevar?: ")
marca_1 = "ArgentinaLuz"
marca_2 = "FelipeLamparas"
resultado = int


# Si el cliente quiere llevar 6 o mas lamparas, se le descuenta un %50
if cant_de_lamparas >= 6:
    Subtotal = cant_de_lamparas * precio_de_las_lamparas # Seria por ejemplo 6*800 = 4800
    descuento = Subtotal * 0.5
    total_a_pagar = Subtotal - descuento
    print("si lleva 6 lamparas: \nEl subtotal es: ", Subtotal, "\nEl descuento es: ", descuento, "\nEl total a pagar es: ", total_a_pagar)
    if total_a_pagar > 4000:
        resultado = total_a_pagar * 0.05
        print("\nPor su excedente a 4000 pesos en total se le aplicara un %5 mas de descuento: \nEl descuento es: ", resultado, "\nEl total a pagar es: ", total_a_pagar - resultado)