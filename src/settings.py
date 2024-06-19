import pygame

# Screen
ANCHO = 1000
ALTO = 600
SCREEN_SIZE = (ANCHO, ALTO)
SCREEN_CENTER = (ANCHO //2, ALTO //2)
MEDIO_ANCHO = ANCHO //2
MEDIO_ALTO = ALTO //2
SUM_SCREEN_CENTER = MEDIO_ANCHO + MEDIO_ALTO

print(SUM_SCREEN_CENTER)

# 1000, 600
# Colors 2467x1696

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CUSTOM = (157, 208, 230)

# Background

y = 0
x = 0

# Performance

FPS = 60
clock = pygame.time.Clock()

# FUNCIONES DE TECLAS

colors = [RED,GREEN,BLUE,CUSTOM]