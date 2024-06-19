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

block = {'rect':pygame.Rect(300,120, 100, 100),'color':RED,'dir':DL}







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
    if block["rect"].right >= ANCHO:
        if block["dir"] == DR:
            block["dir"] = DL
        else:
            block["dir"] = UL
    elif block["rect"].left <= 0:
        if block["dir"] == DL:
            block["dir"] = DR
        else:
            block["dir"] = UR
    elif block["rect"].bottom >= ALTO:
        if block["dir"] == DR:
            block["dir"] = UR
        else: 
            block["dir"] = UL
    elif block["rect"].top <= 0:
        if block["dir"] == UR:
            block["dir"] = DR
        else:
            block["dir"] = DL


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

    SCREEN.blit(fondo,(x,y))
    pygame.draw.rect(SCREEN,block["color"],block["rect"])

    pygame.display.flip()

pygame.quit()
