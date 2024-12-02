import os

# Ruta relativa al archivo
archivo = "Vibe Mountain.mp3"

# Obtener la ruta absoluta
ruta_absoluta = os.path.abspath(archivo)
print(f"La ruta absoluta del archivo es: {ruta_absoluta}")
