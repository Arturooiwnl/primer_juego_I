import pygame
from settings import * # Cosas para las settings 
# import sys (no le gusta al profe)
# sys.exit() # escapar del programa

# DIRECCIONES 

DR = 3
UR = 9
DL = 1
UL = 7

# INDICES 

rect = 0
color = 1
direccion = 2


pygame.init() # Inicia todos los modulos (.display, .mixer, etc )

SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
fondo = pygame.image.load("imagenes/ciudad_bien.png").convert() #.convert se utiliza para optimizar las imagenes y no usar tantos recursos
icon = pygame.image.load("imagenes/escudo_icon.png")
pygame.display.set_caption("Am I a test?") # Cambiar titulo
pygame.display.set_icon(icon) # cambiar icono
# image = pygame.image.load("imagenes/escudo_icon.png")
# image = pygame.transform.scale(image, (50, 50)) # escalar la imagen a 50x50 px

block = [pygame.Rect(300,120, 100, 100),RED,DL]







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
    
    #ACTUALIZAMOS ELEMENTOS
    #ACTUALIZAMOS DIRECCION
    if block[rect].right >= ANCHO:
        if block[direccion] == DR:
            block[direccion] = DL
        else:
            block[direccion] = UL
    elif block[rect].left <= 0:
        if block[direccion] == DL:
            block[direccion] = DR
        else:
            block[direccion] = UR
    elif block[rect].bottom >= ALTO:
        if block[direccion] == DR:
            block[direccion] = UR
        else: 
            block[direccion] = UL
    elif block[rect].top <= 0:
        if block[direccion] == UR:
            block[direccion] = DR
        else:
            block[direccion] = DL


    # ACTUALIZAMOS MOVIMIENTO
    if block[direccion] == DR:
        block[rect].x += speed
        block[rect].y += speed
    elif block[direccion] == DL:
        block[rect].x -= speed
        block[rect].y += speed
    elif block[direccion] == UL:
        block[rect].x -= speed
        block[rect].y -= speed
    elif block[direccion] == UR:
        block[rect].x += speed
        block[rect].y -= speed

    SCREEN.blit(fondo,(x,y))
    pygame.draw.rect(SCREEN,block[color],block[rect])

    pygame.display.flip()

pygame.quit()
