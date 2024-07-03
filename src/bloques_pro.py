import pygame
from random import randint, randrange
from settings import *

def create_block(imagen=None, left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, velocidad=2):
    return {
        "rect": pygame.Rect(left, top, width, height),
        "color": color,
        "img": imagen,
        "dir": dir,
        "velocidad": velocidad,
        "borde": borde,
        "radio": radio
    }

def create_player(imagen=None):
    return create_block(imagen, SCREEN_CENTER[0]-player_w//2, SCREEN_CENTER[1]-player_h//2, player_w, player_h, GREEN, ESTE, 0, player_h//2, 0)

def create_coin(coins, imagen=None):
    coin_width = 50
    coin_height = 50
    while True:
        x = randint(0, WIDTH-coin_width)
        y = randint(0, HEIGHT-coin_height)
        coin_rect = pygame.Rect(x, y, coin_width, coin_height)
        if not any(coin_rect.colliderect(coin["rect"]) for coin in coins):
            break
    velocidad = randrange(1, 3)
    return create_block(imagen, x, y, coin_width, coin_height, YELLLOW, 0, velocidad, coin_height//2)

def load_coin_list(lista, cantidad, imagen=None):
    for _ in range(cantidad):
        lista.append(create_coin(lista, imagen))
