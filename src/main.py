import pygame
from settings import * # Cosas para las settings 
# import sys (no le gusta al profe)
# sys.exit() # escapar del programa

pygame.init() # Inicia todos los modulos (.display, .mixer, etc )

SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
fondo = pygame.image.load("imagenes/ciudad_bien.png").convert() #.convert se utiliza para optimizar las imagenes y no usar tantos recursos
icon = pygame.image.load("imagenes/escudo_icon.png")
pygame.display.set_caption("Am I a test?") # Cambiar titulo
pygame.display.set_icon(icon)


SCREEN.fill(CUSTOM) # Cambiar color de la pantalla .fill((red, green, blue)) maximo de valor de color es 255
SCREEN.blit(fondo,(x,y))
# contador = 0

is_running = True # bandera para decir que esta andando el progragama
while is_running:
    # print(contador)
    # contador += 1 # contador para ver cuanto se itera
    for event in pygame.event.get(): # pygame.event.get() devuelve una lista de los eventos que ocurrieron
        if event.type == pygame.QUIT: # pygame.QUIT = 256, numero del evento para cerrar (quit) | Todos los eventos tienen un valor numérico y aparecen como constante
            is_running = False
    
    x_relativa = x % fondo.get_rect().width
    SCREEN.blit(fondo, (x_relativa - fondo.get_rect().width, y))
    if x_relativa < ANCHO:
        SCREEN.blit(fondo, (x_relativa, y))
    x -= 0.5 # Velocidad del fondo
    # RELOJ.tick(FPS)
    pygame.display.flip() # Voltea la pantalla | actualiza

pygame.quit() # contrario a pygame.init() | Cierra el programa