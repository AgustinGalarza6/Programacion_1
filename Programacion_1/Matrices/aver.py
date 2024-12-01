import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Tamaño de la celda
CELL_SIZE = 60

# Tablero de Sudoku (0 representa espacios vacíos)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

selected_cell = None  # Para almacenar la celda seleccionada

# Función para dibujar el tablero de Sudoku
def draw_board():
    for x in range(0, 9):
        for y in range(0, 9):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Dibuja el borde de la celda

# Función para dibujar números en el tablero
def draw_numbers(board):
    font = pygame.font.Font(None, 74)  # Fuente para los números
    for y in range(9):
        for x in range(9):
            if board[y][x] != 0:  # Si no es un espacio vacío
                text = font.render(str(board[y][x]), True, BLACK)
                screen.blit(text, (x * CELL_SIZE + 20, y * CELL_SIZE + 10))  # Ajusta la posición

# Función para manejar clics del ratón
def handle_mouse_click(pos):
    global selected_cell
    x, y = pos
    cell_x = x // CELL_SIZE
    cell_y = y // CELL_SIZE
    if 0 <= cell_x < 9 and 0 <= cell_y < 9:
        selected_cell = (cell_x, cell_y)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if selected_cell is not None and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                # Obtener el número ingresado
                number = int(event.unicode)
                cell_x, cell_y = selected_cell
                # Solo actualizar si la celda está vacía
                if sudoku_board[cell_y][cell_x] == 0:
                    sudoku_board[cell_y][cell_x] = number  # Actualiza el número en la celda seleccionada

    screen.fill(GRAY)  # Rellenar el fondo
    draw_board()  # Dibuja el tablero
    draw_numbers(sudoku_board)  # Dibuja los números
    pygame.display.flip()