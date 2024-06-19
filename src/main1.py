import pygame
from settings import * # Cosas para las settings 
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

block = pygame.Rect(300,250, 100, 100)
block_dir = UL
block_color = RED

block_2 = pygame.Rect(240,120, 100, 100)
block_dir_2 = UL
block_color_2 = BLUE







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
    if block.right >= ANCHO:
        if block_dir == DR:
            block_dir = DL
        else:
            block_dir = UL
    elif block.left <= 0:
        if block_dir == DL:
            block_dir = DR
        else:
            block_dir = UR
    elif block.bottom >= ALTO:
        if block_dir == DR:
            block_dir = UR
        else: 
            block_dir = UL
    elif block.top <= 0:
        if block_dir == UR:
            block_dir = DR
        else:
            block_dir = DL


    # ACTUALIZAMOS MOVIMIENTO
    if block_dir == DR:
        block.x += speed
        block.y += speed
    elif block_dir == DL:
        block.x -= speed
        block.y += speed
    elif block_dir == UL:
        block.x -= speed
        block.y -= speed
    elif block_dir == UR:
        block.x += speed
        block.y -= speed

    SCREEN.blit(fondo,(x,y))
    pygame.draw.rect(SCREEN,block_color,block)

    pygame.display.flip()

pygame.quit()
