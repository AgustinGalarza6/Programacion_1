import pygame
import constantes
from personaje import Personaje

Player_1 = Personaje(x = 50, y = 50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("Welcome!")

run = True
while run is True:
    Player_1.dibujar(ventana)
    for event in pygame.event.get(): # event (eventos) son todas aquellas acciones que ocurren en el juego.
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Opcion A:
    #pygame.display.update()
    # Opcion B:
    pygame.display.flip()

