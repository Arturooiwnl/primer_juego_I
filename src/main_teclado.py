import pygame
from aleatorios import *
from random import *
from sys import exit
from settings import *
from bloques import *
from math import sqrt
from pygame.locals import *

def mostrar_texto(superficie,texto,fuente,coord,color= RED,color_fondo =BLACK):
    render = fuente.render(texto,False,color,color_fondo)
    rect = render.get_rect()
    rect.center = coord
    superficie.blit(render,rect)

def wait_user(tecla):
    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                if evento.key == tecla:
                    continuar = False

# def wait_user_imagen(imagen):
#     continuar = True
#     while continuar:
#         for evento in pygame.event.get():
#             if evento.type == MOUSEBUTTONDOWN:
#                 if evento.button == imagen:
#                     continuar = False




# flags keys direction

move_left = False
move_right = False
move_up = False
move_down = False


NEWCOINEVENT = USEREVENT +1

pygame.time.set_timer







# inicializar los modulos de pygame
pygame.init()

clock = pygame.time.Clock()

# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")


# Cargo imagenes

img_ovni = pygame.image.load("assets/ovni.png")
asteroide_1 = pygame.image.load("assets/asteroide.png")
asteroide_2 = pygame.image.load("assets/asteroide2.png")



img_background = pygame.transform.scale(pygame.image.load("assets/fondo.jpg"), SCREEN_SIZE)
# SOUNDS
collision_sound = pygame.mixer.Sound("assets/coin.mp3")
playing_music = True

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
block = create_player(img_ovni)

# Creo la lista monedas
coins = []
# Carga la cantidad de monedas(10)
load_coin_list(coins,INITIAL_QTY_COINS,asteroide_1)



score = 0

text = font.render(f"Puntaje : {score}",False,RED)

is_running = True

screen.fill(BLACK)
mostrar_texto(screen,"Asteoroides",font,SCREEN_CENTER,RED,CUSTOM)
mostrar_texto(screen,"Presione SPACE para comenzar",font,(WIDTH//2,HEIGHT-50),CUSTOM)
pygame.display.flip()
wait_user(K_SPACE)



while is_running:
    clock.tick(FPS)
    # ----> detectar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            is_running = False
        # eventos presionar tecla
        if evento.type == KEYDOWN:
            if evento.key == K_LEFT:
                move_left = True
                move_right = False
            if evento.key == K_RIGHT:
                move_right = True
                move_left = False
            if evento.key == K_UP:
                move_up = True
                move_down = False
            if evento.key == K_DOWN:
                move_down = True
                move_up = False
            if evento.key == K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                    mostrar_texto(screen,"Mute",font,(50,HEIGHT-50),)
                else:
                    pygame.mixer.music.unpause()
                playing_music = not playing_music
            if evento.key == K_p:
                if playing_music:
                    pygame.mixer.music.pause()
                    mostrar_texto(screen,"Mute",font,(50,HEIGHT-50),)
                else:
                    pygame.mixer.music.unpause()
                playing_music = not playing_music
        # eventos liberar tecla
        if evento.type == KEYUP:
            if evento.key == K_LEFT:
                move_left = False
            if evento.key == K_RIGHT:
                move_right = False
            if evento.key == K_UP:
                move_up = False
            if evento.key == K_DOWN:
                move_down = False
        if evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:
                new_coin = create_coin()
                new_coin["color"] = RED
                new_coin["rect"].center = evento.pos
                coins.append(new_coin)

# muevo el bloque de acuerdo a su direccion
    if move_left and block["rect"].left > 0:
        block["rect"].left-= SPEED
        if  block["rect"].left < 0:
            block["rect"].left = 0
    elif move_right and block["rect"].right < WIDTH:
        block["rect"].right += SPEED
        if  block["rect"].right > WIDTH:
            block["rect"].right = WIDTH
    elif move_up and block["rect"].top > 0:
        block["rect"].top -= SPEED
        if  block["rect"].top < 0:
            block["rect"].top = 0
    elif move_down and block["rect"].bottom < HEIGHT:
        block["rect"].bottom += SPEED
        if  block["rect"].bottom >HEIGHT:
            block["rect"].bottom = HEIGHT

     # ne fijo si el player choca contra una coin       
    for coin in coins[:]:
        if detectar_colision_circulo(block["rect"], coin["rect"]):
            coins.remove(coin)
            collision_sound.play()
            score+=1
            text = font.render(f"Puntaje : {score}",False,RED)
            # print("Colision!!!!")
            if len(coins) == 0:
                load_coin_list(coins,INITIAL_QTY_COINS,asteroide_2)

    # dibujar pantalla

    screen.blit(img_background, ORIGIN)
    screen.blit(block["img"], block["rect"])
    for coin in coins:
        if coin["img"]:
            screen.blit(coin["img"], coin["rect"])
        else:
            pygame.draw.rect(screen, coin["color"],coin["rect"],border_radius= coin["radio"])

    screen.blit(text,(350,20))
    # actualizo la pantalla

    pygame.display.flip()
pygame.quit()
