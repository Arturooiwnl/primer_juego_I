import pygame
from settings import * # Cosas para los settings 
# import sys (no le gusta al profe)
# sys.exit() # escapar del programa

pygame.init() # Inicia todos los modulos (.display, .mixer, etc )

SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
fondo = pygame.image.load("imagenes/ciudad.jpg")
icon = pygame.image.load("imagenes/escudo_icon.png")
pygame.display.set_caption("Mi primer juego") # Cambiar titulo
pygame.display.set_icon(icon)


SCREEN.fill(CUSTOM) # Cambiar color de la pantalla .fill((red, green, blue)) maximo de valor de color es 255
SCREEN.blit(fondo,(0,0))
# contador = 0

is_running = True # bandera para decir que esta andando el progragama
while is_running:
    # print(contador)
    # contador +=1 | contador para ver cuanto se itera
    for event in pygame.event.get(): # pygame.event.get() # Devuelve una lista de los eventos que ocurrieron
        if event.type == pygame.QUIT: # pygame.QUIT = 256 numero del evento para cerrar (quit) | Todos los eventos tienen un valor numerico y aparecen como constant
            is_running = False

    pygame.display.flip() # Voltea la pantall \ actualiza

pygame.quit() # contrario a pygame.init() | Cierra el programa