import pygame
from settings import * # Cosas para las settings 
from random import randint
from aleatorios import *

# DIRECCIONES
DR = 3
UR = 9
DL = 1
UL = 7

pygame.init()  # Inicia todos los módulos de Pygame

SCREEN = pygame.display.set_mode(SCREEN_SIZE)  # Crear la pantalla (800 ancho, 600 de alto)
fondo = pygame.image.load("imagenes/ciudad_bien.png").convert()  # Optimizar la imagen
icon = pygame.image.load("imagenes/escudo_icon.png")
pygame.display.set_caption("Am I a test?")  # Cambiar título
pygame.display.set_icon(icon)  # Cambiar ícono

block_ancho = 100
block_alto = 100

blocks = [{'rect': pygame.Rect(randint(0, ANCHO - block_ancho), randint(0, ALTO - block_alto), block_ancho, block_alto), 'color': RED, 'dir': DL, 'borde': 0, 'radio': -1},
          {'rect': pygame.Rect(randint(0, ANCHO - block_ancho), randint(0, ALTO - block_alto), block_ancho, block_alto), 'color': BLUE, 'dir': DR, 'borde': 0, 'radio': -1},
          {'rect': pygame.Rect(randint(0, ANCHO - block_ancho), randint(0, ALTO - block_alto), block_ancho, block_alto), 'color': GREEN, 'dir': UR, 'borde': 0, 'radio': -1}]

font = pygame.font.SysFont("Arial", 74)  # Usar una fuente específica pasando la ruta del archivo de fuente
text = font.render('Hola, Pygame!', True, (255, 255, 255))

# Posición del texto
text_rect = text.get_rect(center=(400, 300))

# Función para dibujar un botón
def draw_button(surface, color, rect, text):
    pygame.draw.rect(surface, color, rect)
    font = pygame.font.SysFont("Arial", 30)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 2))
    surface.blit(text_surface, text_rect)

# Función para comprobar si se hace clic en el botón
def button_clicked(rect, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if rect.collidepoint(event.pos):
            return True
    return False

button_rect = pygame.Rect(350, 500, 100, 50)

speed = 5
gravedad = True

clock = pygame.time.Clock()

is_running = True
while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if button_clicked(button_rect, event):
            print("Button clicked!")

    # Dibujar el fondo
    SCREEN.blit(fondo, (0, 0))

    # Dibujar el texto
    SCREEN.blit(text, text_rect)

    # Dibujar el botón
    draw_button(SCREEN, (0, 128, 255), button_rect, "Click me")

    # Actualizar elementos
    for block in blocks:
        if block["rect"].right >= ANCHO:
            if block["dir"] == DR:
                block["dir"] = DL
            else:
                block["dir"] = UL
            block["color"] = get_random_color(colors)
        elif block["rect"].left <= 0:
            if block["dir"] == DL:
                block["dir"] = DR
            else:
                block["dir"] = UR
            block["color"] = get_random_color(colors)
        elif block["rect"].bottom >= ALTO:
            if block["dir"] == DR:
                block["dir"] = UR
            else:
                block["dir"] = UL
            block["borde"] = randint(0, 10)
        elif block["rect"].top <= 0:
            if block["dir"] == UR:
                block["dir"] = DR
            else:
                block["dir"] = DL
            block["radio"] = randint(-1, 20)

        # Actualizar movimiento
        if block["dir"] == DR:
            block["rect"].x += speed
            block["rect"].y += speed
        elif block["dir"] == DL:
            block["rect"].x -= speed
            block["rect"].y += speed
        elif block["dir"] == UL:
            block["rect"].x -= speed
            block["rect"].y -= speed
        elif block["dir"] == UR:
            block["rect"].x += speed
            block["rect"].y -= speed

    # Dibujar bloques
    for block in blocks:
        pygame.draw.rect(SCREEN, block["color"], block["rect"], block["borde"], block["radio"])

    pygame.display.flip()

pygame.quit()
