'''
La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

CONFECCIÓN DE UN COMETA: 



Medidas:

AB = Diágonal mayor

DC = Diágonal menor

BD y BC = lados menores

AD y AC = lados mayores

El usuario ingresará las medidas  BC, CD y DA.

Detalles de construcción

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

'''
import math

# Entrada de datos
bc = float(input("Ingrese la medida BC en centímetros: "))
cd = float(input("Ingrese la medida CD en centímetros: "))
da = float(input("Ingrese la medida DA en centímetros: "))

# Calcular la diagonal mayor AB usando Pitágoras en centímetros y aplicando la funcion math.sqrt para calcular la raiz cuadrada
ab = math.sqrt(da**2 + bc**2)

# Calcular el perímetro del cometa (varillas de plástico) en centímetros
perimetro = 2 * (bc + cd)

# Calcular el área del cuerpo del cometa (papel necesario) en centímetros cuadrados
area_cuerpo = (da * ab) / 2.0

# Calcular el área adicional para la cola del cometa en centímetros cuadrados
area_cola = area_cuerpo * 0.1

# Calcular cantidades para 10 cometas en centímetros
varillas_plastico = perimetro * 10
papel_cm2 = (area_cuerpo + area_cola) * 10

# Mostrar resultados en centímetros
print(f"Se necesitan {varillas_plastico:.2f} centímetros de varillas de plástico.")
print(f"Se necesitan {papel_cm2:.2f} centímetros cuadrados de papel.")