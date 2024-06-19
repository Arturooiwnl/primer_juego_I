from random import randint,randrange

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CUSTOM = (157, 208, 230)

colors = [RED,GREEN,BLUE,CUSTOM]


def get_random_element(lista:list)->any:
    i = randint(0, len(lista) -1)
    el = lista[i]
    return el

def get_random_color(colors:list)->tuple[int, int, int]:
    return get_random_element(colors)

def random_color()->tuple[int, int, int]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)