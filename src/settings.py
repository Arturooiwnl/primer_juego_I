import pygame

# Screen
WIDTH = 800
HEIGHT = 600
MID_WIDTH = WIDTH//2
MID_HEIGHT = HEIGHT//2
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (WIDTH // 2, HEIGHT // 2)
ORIGIN = (0, 0)
POS_PLAY_BUTTON = (MID_WIDTH,MID_HEIGHT//2)

# 1000, 600
# Colors 2467x1696

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLLOW = (255, 255, 0)
CUSTOM = (100, 100, 100)
# Background

y = 0
x = 0

# Performance

FPS = 60
clock = pygame.time.Clock()

# FUNCIONES DE TECLAS

colors = [RED,GREEN,BLUE,CUSTOM]

SPEED = 5
INITIAL_QTY_COINS = 10
MAX_QTY_COINS = 30


rect_w = 50
rect_h = 50



FPS = 60

INITIAL_QTY_COINS = 10
MAX_QTY_COINS = 30

player_w = 70
player_h = 70
player_d = 3
SPEED = 5

# Directions
direcciones = [0,1,2,3]
NORTE = 0
ESTE = 1
SUR = 2
OESTE = 3