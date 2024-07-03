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

def create_coin(imagen=None,visible= True):
    coin_width = 30
    coin_height = 30
    velocidad = 2  # Velocidad de la moneda
    if visible:
        y =  randint(0, HEIGHT-coin_height)
    else:
        y =  0 - randint(0, HEIGHT-coin_height)
    if imagen:
        imagen = pygame.transform.scale(imagen, (coin_width, coin_height))
    a = create_block(imagen, randint(0, WIDTH-coin_width), y, coin_width, coin_height, YELLLOW, 0, velocidad, coin_height//2)
    a["velocidad"] = randint(min_speed_asteroid,max_speed_asteroid)
    return a

def create_laser(midbottom=(0,0),color = RED):
    rect = pygame.Rect(0,0,laser_w,laser_h)
    rect.midbottom = midbottom
    return {"rect": rect, "color": color,"velocidad":laser_speed}






def load_coin_list(lista, cantidad, imagen=None):
    for _ in range(cantidad):
        lista.append(create_coin(imagen,False))
