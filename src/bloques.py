import pygame
from random import randint, randrange
from settings import *

def create_block(imagen=None, left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, velocidad=2):
    return {
        "rect": pygame.Rect(left, top, width, height),
        "color": color,
        "dir": dir,
        "borde": borde,
        "radio": radio,
        "img": imagen,
        "velocidad": velocidad
    }

def create_player(imagen=None):
    if imagen:
        imagen = pygame.transform.scale(imagen, (player_w, player_h))
    return create_block(imagen, randint(0, WIDTH - player_w), randint(0, HEIGHT - player_h), player_w, player_h, dir=direcciones[randrange(len(direcciones))], color=randint(0, WIDTH - player_w))

def create_coin(imagen=None):
    coin_width = 30
    coin_height = 30
    velocidad = 2  # Velocidad de la moneda
    if imagen:
        imagen = pygame.transform.scale(imagen, (coin_width, coin_height))
    return create_block(imagen, randint(0, WIDTH-coin_width), randint(0, HEIGHT-coin_height), coin_width, coin_height, YELLLOW, 0, velocidad, coin_height//2)

def load_coin_list(lista, cantidad, imagen=None):
    for _ in range(cantidad):
        lista.append(create_coin(imagen))
