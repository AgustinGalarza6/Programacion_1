clientes = []

def registrar_cliente(nombre, apellido, DNI):
    cliente = {
        'nombre': nombre,
        'apellido': apellido,
        "DNI": DNI,
        'Mascotas': []
    }
    clientes.append(cliente)
    print(f"\nEl cliente se ha sido registrado correctamente.\n")

def agregar_mascota(DNI, nombre, tipo):
    for cliente in clientes:
        if cliente['DNI'] == DNI:
            mascota = {
                'nombre': nombre,
                'tipo': tipo
            }
            cliente['Mascotas'].append(mascota)
            print(f"\nLa mascota se ha sido registrada correctamente.\n")
            return
    print("El cliente no encontrado")


def listar_clientes():
    if not clientes:
        print("No hay clientes registrados")
    else:
        for cliente in clientes:
            print(f"Cliente: {cliente['nombre']} {cliente['apellido']}, DNI: {cliente['DNI']}\n")
            n = 1
            for mascota in cliente['Mascotas']:
                print(f"Mascota {n}: ")
                print(f"Nombre: {mascota['nombre']}, Tipo: {mascota['tipo']}\n")
                n += 1

def imprimir_historial_visitas(DNI):
    for cliente in clientes:
        if cliente['DNI'] == DNI:
            filename = f"{cliente['nombre']}_{cliente['apellido']}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                for mascota in cliente['Mascotas']:
                    file.write(f"Visita para: {mascota['nombre']}, Tipo: {mascota['tipo']}\n")
                    file.write("Fecha 6/9/2024, Hora: 18:00hs,\nResumen: Visita de chequeo general\n\n")
                print(f"\nHistorial de visitas guardado en {filename}\n")
                return
        print("El cliente no encontrado")

def main():
    while True:
        print("1. Registrar cliente")
        print("2. Agregar mascota a un cliente")
        print("3. Listar todos los clientes con sus mascotas")
        print("4. Imprimir historial de visitas de una mascota")
        print("5. Salir del programa")
        opcion = input("\nIngresa una opción: \n")
        if opcion == "1":
            nombre = input("Ingresa el nombre: ")
            apellido = input("Ingresa el apellido: ")
            DNI = input("Ingresa el DNI: ")
            registrar_cliente(nombre, apellido, DNI)
        elif opcion == "2":
            DNI = input("Ingresa el DNI del cliente: ")
            nombre = input("Ingresa el nombre de la mascota: ")
            tipo = input("Ingresa el tipo de la mascota: ")
            agregar_mascota(DNI, nombre, tipo)
        elif opcion == "3":
            listar_clientes()
        elif opcion == "4":
            DNI = input("Ingresa el DNI del cliente: ")
            imprimir_historial_visitas(DNI)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion inválida. Por favor seleccione nuevamente.")

main()