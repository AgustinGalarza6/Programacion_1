import json 
import os

def leer_json(nombre_archivo:str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            lista_puntajes = json.load(archivo)
    else:
        lista_puntajes = []
        
    return lista_puntajes


def guardar_json(nombre_archivo: str, nuevo_puntaje: dict):
    try:
        # Intentar leer el archivo para obtener los puntajes existentes
        with open(nombre_archivo, "r") as archivo:
            lista_puntajes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío, inicializar una lista vacía
        lista_puntajes = []

    # Asegurarte de que lista_puntajes sea una lista plana
    if isinstance(lista_puntajes, list) and all(isinstance(i, dict) for i in lista_puntajes):
        lista_puntajes.append(nuevo_puntaje)  # Agregar el nuevo puntaje
    else:
        lista_puntajes = [nuevo_puntaje]  # Corregir si no es una lista válida

    # Guardar nuevamente en el archivo JSON
    with open(nombre_archivo, "w") as archivo:
        json.dump(lista_puntajes, archivo, indent=4)

