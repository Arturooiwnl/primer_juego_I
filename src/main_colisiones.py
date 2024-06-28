import pygame
from aleatorios import *
from random import *
from sys import exit
from settings import *
from bloques import *
from math import sqrt

# inicializar los modulos de pygame
pygame.init()

clock = pygame.time.Clock()

gravedad_y = True
gravedad_x = True

# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

# configuro la direccion
UR = 9
DR = 3
DL = 1
UL = 7

direcciones = (UR, DR, DL, UL)


rect_w = 100
rect_h = 100
count_blocks = 2

def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def detectar_colision(rect_1, rect_2):
    for r1, r2 in [(rect_1,rect_2),(rect_2,rect_1)]:
        if punto_en_rectangulo(r1.topleft,r2) or \
            punto_en_rectangulo(r1.topright,r2) or \
            punto_en_rectangulo(rect_1.bottomleft, r2) or\
            punto_en_rectangulo(rect_1.bottomright, r2):
            return True
        else:
            return False


def distancia_entre_puntos(pto_1:tuple[int, int], pto_2:tuple[int, int]) -> float :
    base = pto_1[0] - pto_2[0]
    altura = pto_1[1] - pto_2[1]
    return (base ** 2 + altura ** 2) ** 0.5

        
def calcular_radio(rect):
    return rect.width // 2

        
def detectar_colision_circulo(rect_1, rect_2) -> bool :
    r1 = calcular_radio(rect_1)
    r2 = calcular_radio(rect_2)
    base = rect_1.centerx - rect_2.centerx
    altura = rect_1.centery - rect_2.centery
    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
    return distancia <= r1 + r2


# Fuente
font = pygame.font.SysFont(None, 30)


# Creo el player
block = create_player()

# Creo la lista monedas
coins = []
# Carga la cantidad de monedas(10)
load_coin_list(coins,INITIAL_QTY_COINS)



score = 0

text = font.render(f"Puntaje : {score}",False,RED)

is_running = True

while is_running:
    clock.tick(FPS)
    # ----> detectar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False

    # ----> actualizar los elementos

# verifico si el bloque choca contra los limites de la pantalla
# actualizo su direccion
    if block["rect"].right >= WIDTH:
        # choco derecha
        if block["dir"] == DR:
            block["dir"] = DL
        elif block["dir"] == UR:
            block["dir"] = UL
        block["color"] = random_color()
    elif block["rect"].left <= 0:
        # choco izquierda
        if block["dir"] == UL:
            block["dir"] = UR
        elif block["dir"] == DL:
            block["dir"] = DR
        block["borde"] = randrange(31)
    elif block["rect"].top <= 0:
        # choco arriba
        if block["dir"] == UL:
            block["dir"] = DL
        elif block["dir"] == UR:
            block["dir"] = DR
    elif block["rect"].bottom >= HEIGHT:
        # choco abajo
        if block["dir"] == DR:
            block["dir"] = UR
        elif block["dir"] == DL:
            block["dir"] = UL
        # block["radio"] = randint(-1, 25)


# muevo el bloque de acuerdo a su direccion
    if block["dir"] == DR:
        block["rect"].top += SPEED
        block["rect"].left += SPEED
    elif block["dir"] == DL:
        block["rect"].top += SPEED
        block["rect"].left -= SPEED
    elif block["dir"] == UL:
        block["rect"].top -= SPEED
        block["rect"].left -= SPEED
    elif block["dir"] == UR:
        block["rect"].top -= SPEED
        block["rect"].left += SPEED

    for coin in coins[:]:
        if detectar_colision_circulo(block["rect"], coin["rect"]):
            coins.remove(coin)
            score+=1
            text = font.render(f"Puntaje : {score}",False,RED)
            print("Colision!!!!")
            if len(coins) == 0:
                load_coin_list(coins,INITIAL_QTY_COINS)

    # dibujar pantalla

    screen.fill(BLACK)
    screen.blit(text,(350,20))
    pygame.draw.rect(
            screen, block["color"], block["rect"], block["borde"], block["radio"])

    for coin in coins:
        pygame.draw.rect(screen, coin["color"],coin["rect"],border_radius= coin["radio"])

    # actualizo la pantalla

    pygame.display.flip()

pygame.quit()
