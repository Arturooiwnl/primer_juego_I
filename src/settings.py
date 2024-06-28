import pygame

# Screen
WIDTH = 1000
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (WIDTH //2, HEIGHT //2)
MEDIO_WIDTH = WIDTH //2
MEDIO_HEIGHT = HEIGHT //2
SUM_SCREEN_CENTER = MEDIO_WIDTH + MEDIO_HEIGHT

ORIGIN = (0,0)

print(SUM_SCREEN_CENTER)

# 1000, 600
# Colors 2467x1696

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
CUSTOM = (157, 208, 230)
YELLLOW = (255,255,0)

# Background

y = 0
x = 0

# Performance

FPS = 60
clock = pygame.time.Clock()

# FUNCIONES DE TECLAS

colors = [RED,GREEN,BLUE,CUSTOM]

SPEED = 5
INITIAL_QTY_COINS = 30


UR = 9
DR = 3
DL = 1
UL = 7

direcciones = (UR, DR, DL, UL)

rect_w = 50
rect_h = 50
player_w = 50
player_h = 50