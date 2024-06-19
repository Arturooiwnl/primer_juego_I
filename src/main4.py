import pygame
from settings import * # Cosas para las settings 
from random import randint
from aleatorios import *
# import sys (no le gusta al profe)
# sys.exit() # escapar del programa

# DIRECCIONES 

DR = 3
UR = 9
DL = 1
UL = 7


pygame.init() # Inicia todos los modulos (.display, .mixer, etc )

SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
fondo = pygame.image.load("imagenes/ciudad_bien.png").convert() #.convert se utiliza para optimizar las imagenes y no usar tantos recursos
icon = pygame.image.load("imagenes/escudo_icon.png")
pygame.display.set_caption("Am I a test?") # Cambiar titulo
pygame.display.set_icon(icon) # cambiar icono
# image = pygame.image.load("imagenes/escudo_icon.png")
# image = pygame.transform.scale(image, (50, 50)) # escalar la imagen a 50x50 px

block_ancho = 100
block_alto = 100

blocks = [{'rect':pygame.Rect(randint(0, ANCHO - block_ancho),randint(0, ALTO - block_alto), block_alto, block_ancho),'color':RED,'dir':DL,'borde':0,'radio': -1},
         {'rect':pygame.Rect(randint(0, ANCHO - block_ancho),randint(0, ALTO - block_alto), block_alto, block_ancho),'color':BLUE,'dir':DR,'borde':0,'radio': -1},
         {'rect':pygame.Rect(randint(0, ANCHO - block_ancho),randint(0, ALTO - block_alto), block_alto, block_ancho),'color':GREEN,'dir':UR,'borde':0,'radio': -1}]

font = pygame.font.SysFont("Arial",74)  # Puedes usar una fuente específica pasando la ruta del archivo de fuente
text = font.render('Hola, Pygame!', True, (255, 255, 255))

# Posición del texto
text_rect = text.get_rect(center=(400, 300))





speed = 5
gravedad = True



SCREEN.fill(CUSTOM) # Cambiar color de la pantalla .fill((red, green, blue)) maximo de valor de color es 255
SCREEN.blit(fondo,(x,y))

is_running = True
while is_running:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    SCREEN.blit(fondo,(x,y))
    SCREEN.blit(text, text_rect)
    #ACTUALIZAMOS ELEMENTOS
    #ACTUALIZAMOS DIRECCION
    for block in blocks:
        if block["rect"].right >= ANCHO:
            if block["dir"] == DR:
                block["dir"] = DL
            else:
                block["dir"] = UL
                block["colors"] = get_random_color(colors)
        elif block["rect"].left <= 0:
            if block["dir"] == DL:
                block["dir"] = DR
            else:
                block["dir"] = UR
            block["colors"] = random_color()
        elif block["rect"].bottom >= ALTO:
            if block["dir"] == DR:
                block["dir"] = UR
            else: 
                block["dir"] = UL
            block["borde"] = randint(0,10)
        elif block["rect"].top <= 0:
            if block["dir"] == UR:
                block["dir"] = DR
            else:
                block["dir"] = DL
            block["radio"] = randint(-1,20) 


        # ACTUALIZAMOS MOVIMIENTO
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
    for block in blocks:
        pygame.draw.rect(SCREEN,block["color"],block["rect"],block["borde"],block["radio"])

    pygame.display.flip()

pygame.quit()
