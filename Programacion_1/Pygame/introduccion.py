import pygame
import os

# Inicializamos pygame y el mixer de música
pygame.init() 
pygame.mixer.init()  # Agregar los paréntesis para inicializar correctamente el mixer

# Tamaños y ubicaciones: X, Y 
ancho_pantalla = 800
largo_pantalla = 600

# Crear la ventana del juego
pantalla = pygame.display.set_mode((ancho_pantalla, largo_pantalla)) 
pygame.display.set_caption("Mi superJuego")
juego_corriendo = True

# AGREGAR MUSICA

# Verificamos si el archivo de música existe
pygame.mixer.music.load("D:/UTN/Programacion_1/Pygame/musica/Vibe Mountain.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

# Bucle principal del juego
while juego_corriendo:
    lista_eventos = pygame.event.get()  # Obtenemos todos los eventos del juego
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:  # Si el evento es salir del juego
            juego_corriendo = False  # Cambiamos la bandera a False para terminar el bucle
    
    # RGB -> Red, Green, Blue. Van del 0 al 255
    pantalla.fill((118, 182, 184))  # Rellenamos la pantalla con un color de fondo
    
    # Actualizamos la pantalla
    pygame.display.flip()  # Siempre al final del bucle para actualizar toda la pantalla

# Mensaje cuando se cierra el juego
print("Se termino el juego")


