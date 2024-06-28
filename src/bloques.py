import pygame
from random import randint,randrange
from settings import *

def create_block(left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1):
    return {"rect": pygame.Rect(left, top, width, height)
            , "color": color, "dir": dir, "borde": borde, "radio": radio}


def create_player():
    rect_w = 50
    rect_h = 50
    return create_block(randint(0, WIDTH - rect_w), randint(0, HEIGHT -
                rect_h), rect_w, rect_h, dir = direcciones[randrange(len(direcciones))], color = randint(0, WIDTH - rect_w))

def create_coin():
    coin_width = 30
    coin_height = 30
    return create_block(randint(0, WIDTH-coin_width)
                        ,randint(0, HEIGHT-coin_height)
                        ,coin_width,coin_height,YELLLOW,0, 0,coin_height//2)

def load_coin_list(lista:list,cant:int):
    for _ in range(cant):
        lista.append(create_coin())