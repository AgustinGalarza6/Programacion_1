import pygame
import random
import sys

# Configuración
ANCHO = 400
ALTO = 400
CELDA = 40
COLUMNAS = ANCHO // CELDA
FILAS = ALTO // CELDA
MINAS = 10

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_CLARO = (200, 200, 200)
GRIS_OSCURO = (150, 150, 150)
ROJO = (255, 0, 0)

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Buscaminas")
fuente = pygame.font.Font(None, 36)

# Generar tablero
def generar_tablero():
    tablero = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
    minas_colocadas = 0
    while minas_colocadas < MINAS:
        x = random.randint(0, COLUMNAS - 1)
        y = random.randint(0, FILAS - 1)
        if tablero[y][x] != -1:
            tablero[y][x] = -1
            minas_colocadas += 1
            # Actualizar números vecinos
            for i in range(max(0, y - 1), min(FILAS, y + 2)):
                for j in range(max(0, x - 1), min(COLUMNAS, x + 2)):
                    if tablero[i][j] != -1:
                        tablero[i][j] += 1
    return tablero

# Dibujar tablero
def dibujar_tablero(tablero, revelado, marcadas):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            rect = pygame.Rect(x * CELDA, y * CELDA, CELDA, CELDA)
            if revelado[y][x]:
                pygame.draw.rect(pantalla, GRIS_CLARO, rect)
                if tablero[y][x] == -1:
                    pygame.draw.circle(pantalla, ROJO, rect.center, CELDA // 4)
                elif tablero[y][x] > 0:
                    texto = fuente.render(str(tablero[y][x]), True, NEGRO)
                    pantalla.blit(texto, texto.get_rect(center=rect.center))
            else:
                pygame.draw.rect(pantalla, GRIS_OSCURO, rect)
                if marcadas[y][x]:
                    pygame.draw.circle(pantalla, NEGRO, rect.center, CELDA // 6)
            pygame.draw.rect(pantalla, NEGRO, rect, 1)

# Verificar si se gana
def verificar_victoria(tablero, revelado):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            if tablero[y][x] != -1 and not revelado[y][x]:
                return False
    return True

# Lógica principal
def main():
    tablero = generar_tablero()
    revelado = [[False for _ in range(COLUMNAS)] for _ in range(FILAS)]
    marcadas = [[False for _ in range(COLUMNAS)] for _ in range(FILAS)]
    juego_terminado = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
                x, y = evento.pos
                x //= CELDA
                y //= CELDA
                if evento.button == 1:  # Click izquierdo
                    if not marcadas[y][x]:
                        revelado[y][x] = True
                        if tablero[y][x] == -1:
                            juego_terminado = True
                elif evento.button == 3:  # Click derecho
                    marcadas[y][x] = not marcadas[y][x]

        pantalla.fill(NEGRO)
        dibujar_tablero(tablero, revelado, marcadas)

        if juego_terminado:
            texto = fuente.render("¡Perdiste!", True, ROJO)
            pantalla.blit(texto, texto.get_rect(center=(ANCHO // 2, ALTO // 2)))
        elif verificar_victoria(tablero, revelado):
            texto = fuente.render("¡Ganaste!", True, BLANCO)
            pantalla.blit(texto, texto.get_rect(center=(ANCHO // 2, ALTO // 2)))
            juego_terminado = True

        pygame.display.flip()

if __name__ == "__main__":
    main()