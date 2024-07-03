import pygame
from aleatorios import *
from random import *
from sys import exit
from settings import *
from bloques import *
from math import sqrt
from pygame.locals import *
from sys import exit



def terminar():
    pygame.quit()
    exit()

def mostrar_texto(superficie,texto,fuente,coord,color= RED,color_fondo =None):
    render = fuente.render(texto,False,color,color_fondo)
    rect = render.get_rect()
    rect.center = coord
    superficie.blit(render,rect)
    pygame.display.flip()

def wait_user(tecla):
    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == tecla:
                    continuar = False

def wait_user_click(rect_img: pygame.Rect):
    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == MOUSEBUTTONDOWN:
                if evento.type == QUIT:
                    terminar()
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos,rect_img):
                        continuar = False




# flags keys direction

move_left = False
move_right = False
move_up = False
move_down = False


# NEWCOINEVENT = USEREVENT +1

# pygame.time.set_timer







# inicializar los modulos de pygame
pygame.init()

clock = pygame.time.Clock()

# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")
pygame.display.set_icon(pygame.image.load("./src/assets/imagenes/nave-espacial.png"))


# Cargo imagenes

img_ovni = pygame.image.load("./src/assets/imagenes/ovni.png")
asteroide_1 = pygame.image.load("./src/assets/imagenes/asteroide.png")
asteroide_2 = pygame.image.load("./src/assets/imagenes/asteroide2.png")



img_background = pygame.transform.scale(pygame.image.load("./src/assets/imagenes/fondo.jpg"), SCREEN_SIZE)
img_start_button = pygame.transform.scale(pygame.image.load("./src/assets/imagenes/start_button.png"), (250,250))


start_button_center_rect = img_start_button.get_rect(center=POS_PLAY_BUTTON)
# SOUNDS
collision_sound = pygame.mixer.Sound("./src/assets/sounds/coin.mp3")
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


fuente_2 = pygame.font.Font("./src/assets/font/dash-horizon.otf",50)


score = 0

text = font.render(f"Puntaje : {score}",False,RED)

is_running = True

pygame.mouse.set_visible(True)
screen.fill(BLACK)
mostrar_texto(screen,"Asteoroides",font,SCREEN_CENTER,RED,CUSTOM)
screen.blit(img_start_button,start_button_center_rect)
pygame.display.flip()
wait_user_click(start_button_center_rect)
# screen.fill(BLACK)
# mostrar_texto(screen,"Asteoroides",font,SCREEN_CENTER,RED,CUSTOM)
# mostrar_texto(screen,"Presione SPACE para comenzar",font,(WIDTH//2,HEIGHT-50),CUSTOM)
# pygame.display.flip()
# wait_user(K_SPACE)
pygame.mouse.set_visible(False)

count_game_over = TIME_GAME

vida_nave = 3
laser=None

while is_running:
    # if count_game_over > 0:
    #     count_game_over-=1
    # else:
    #     is_running = False

    clock.tick(FPS)
    # ----> detectar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            is_running = False
        # eventos presionar tecla
        if evento.type == KEYDOWN:
            if evento.key == K_f:
                if not laser:
                    laser = create_laser(block["rect"].midtop)
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
                mostrar_texto(screen,"PAUSA",fuente_2,SCREEN_CENTER,CUSTOM)
                wait_user(K_p)
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
        if evento.type == MOUSEMOTION:
            block["rect"].center = evento.pos

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
    
    pygame.mouse.set_pos(block["rect"].center)

    for coin in coins:
        coin["rect"].move_ip(0, coin["velocidad"])
        if coin["rect"].top > HEIGHT:
            coin["rect"].bottom = 0

        if laser:
            laser["rect"].move_ip(0, -laser["velocidad"])
            if laser["rect"].bottom <0:
                laser = None
     
    for coin in coins[:]:
        if laser:
            if detectar_colision_circulo(laser["rect"], coin["rect"]):
                coins.remove(coin)
                laser = None
                collision_sound.play()
                score+=1
                text = font.render(f"Puntaje : {score}",False,RED)
                if len(coins) == 0:
                    load_coin_list(coins,INITIAL_QTY_COINS,asteroide_2)
            if detectar_colision_circulo(block["rect"], coin["rect"]):
                coins.remove(coin)
                vida_nave-=1
                # if vida_nave == 0:
                #     is_running = False

    # dibujar pantalla

    screen.blit(img_background, ORIGIN)
    screen.blit(block["img"], block["rect"])
    for coin in coins:
        if coin["img"]:
            screen.blit(coin["img"], coin["rect"])
        else:
            pygame.draw.rect(screen, coin["color"],coin["rect"],border_radius= coin["radio"])

    if laser:
        pygame.draw.rect(screen,laser["color"],laser["rect"])

    screen.blit(text,(350,20))
    # actualizo la pantalla

    pygame.display.flip()

    # mostrar_texto(screen,"GAME OVER",fuente_2,SCREEN_CENTER,RED,CUSTOM)
    # mostrar_texto(screen,"Presione SPACE para continuar",fuente_2,(WIDTH//2,HEIGHT-50),CUSTOM)
    # pygame.display.flip()wd



pygame.quit()
