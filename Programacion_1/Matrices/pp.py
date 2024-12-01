import pygame
import sys
import random
import time
import json

pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
LIGHT_GRAY = (220, 220, 220)

# Fuentes
FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 72)

# # Recursos
# BACKGROUND_IMAGE = pygame.image.load("imagenes/background.jpg")
# MUSIC = "background_music.mp3"  # Música de fondo
# pygame.mixer.music.load(MUSIC)
# pygame.mixer.music.play(-1)

# Variables globales
tablero = None
nivel_dificultad = "Fácil"
dificultad_ocultacion = {"Fácil": 20, "Intermedio": 40, "Difícil": 60}
nombre_jugador = ""
puntajes = []

# Funciones auxiliares
def dibujar_texto(texto, fuente, color, superficie, x, y):
    text = fuente.render(texto, True, color)
    rect = text.get_rect(center=(x, y))
    superficie.blit(text, rect)

def generar_tablero_sudoku():
    """Genera un tablero de Sudoku válido."""
    # Implementa la lógica de Sudoku o un generador básico
    return [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]

def ocultar_celdas(tablero, porcentaje):
    """Oculta celdas del tablero según el porcentaje."""
    total_celdas = 81
    celdas_a_ocultar = (porcentaje * total_celdas) // 100
    tablero_oculto = [fila[:] for fila in tablero]
    while celdas_a_ocultar > 0:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if tablero_oculto[fila][columna] != 0:
            tablero_oculto[fila][columna] = 0
            celdas_a_ocultar -= 1
    return tablero_oculto

def guardar_puntajes(puntajes):
    with open("puntajes.json", "w") as file:
        json.dump(puntajes, file)

def cargar_puntajes():
    try:
        with open("puntajes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Pantallas
def pantalla_inicio():
    global nivel_dificultad
    while True:
        # SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
        # dibujar_texto("Sudoku", LARGE_FONT, WHITE, SCREEN, WIDTH // 2, HEIGHT // 6)

        botones = [
            ("Jugar", WIDTH // 2, HEIGHT // 3),
            ("Puntajes", WIDTH // 2, HEIGHT // 2),
            ("Salir", WIDTH // 2, 2 * HEIGHT // 3),
        ]

        dificultades = ["Fácil", "Intermedio", "Difícil"]
        for i, dif in enumerate(dificultades):
            color = BLUE if dif == nivel_dificultad else GRAY
            pygame.draw.rect(SCREEN, color, (WIDTH // 2 - 100 + i * 120, HEIGHT - 100, 100, 50))
            dibujar_texto(dif, FONT, WHITE, SCREEN, WIDTH // 2 - 50 + i * 120, HEIGHT - 75)

        for texto, x, y in botones:
            pygame.draw.rect(SCREEN, GRAY, (x - 100, y - 25, 200, 50))
            dibujar_texto(texto, FONT, BLACK, SCREEN, x, y)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Botón Jugar
                if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT // 3 - 25 <= y <= HEIGHT // 3 + 25:
                    return "jugar"
                # Botón Puntajes
                elif WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT // 2 - 25 <= y <= HEIGHT // 2 + 25:
                    return "puntajes"
                # Botón Salir
                elif WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and 2 * HEIGHT // 3 - 25 <= y <= 2 * HEIGHT // 3 + 25:
                    pygame.quit()
                    sys.exit()
                # Selección de dificultad
                for i, dif in enumerate(dificultades):
                    if WIDTH // 2 - 100 + i * 120 <= x <= WIDTH // 2 - 100 + i * 120 + 100 and HEIGHT - 100 <= y <= HEIGHT - 50:
                        nivel_dificultad = dif

# Programa principal
def main():
    global puntajes
    puntajes = cargar_puntajes()

    while True:
        pantalla = pantalla_inicio()
        if pantalla == "jugar":
            print("Aquí se inicia la pantalla de juego")
        elif pantalla == "puntajes":
            print("Mostrar puntajes")
        # Aquí seguirías implementando las demás pantallas y funcionalidades.

if __name__ == "__main__":
    main()