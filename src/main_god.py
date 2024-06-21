import pygame
import sys


# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("imagenes/principal/ciudad_bien.png")
icon = pygame.image.load("imagenes/principal/escudo_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Tycoon Game")


# Configurar el reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# Variables globales
money = 1000
resources = 0
resources_list = [
    {"index":1,"mat": "Madera", "precio": 20},
    {"index":2,"mat": "Piedra", "precio": 30},
    {"index":3,"mat": "Agua", "precio": 15},
    {"index":4,"mat": "Metal", "precio": 50}
]

# Funciones para manipular las variables
def add_money(amount):
    global money
    money += amount

def spend_money(amount):
    global money
    if money >= amount:
        money -= amount
        return True
    return False

def add_resources(amount):
    global resources
    resources += amount

def remove_resources(amount):
    global resources
    if resources >= amount:
        resources -= amount
        return True
    return False

# def draw_menu(screen):

#     pygame.draw.rect(screen, LIGHT_BLUE, menu_resources,0,10)

#     font = pygame.font.SysFont(None, 20)
#     for resource in resources_list:
#         resources_list_txt = font.render(f"Material: {resource["mat"]}", True, NEGRO) 
#         resource_rect = resources_list_txt.get_rect(center=menu_resources.center)
#         screen.blit(resources_list_txt, resource_rect)

# Función para dibujar la UI
def draw_ui(screen):
    screen.blit(fondo,(0,0))
    font = pygame.font.SysFont(None, 50)
    money_text = font.render(f"Dinero: ${money}", True, NEGRO)
    resources_text = font.render(f"Recursos: {resources}", True, NEGRO)
    screen.blit(money_text, (10, 10))
    screen.blit(resources_text, (10, 40))
    # Dibujar botón
    pygame.draw.rect(screen, GREEN, sell_button,0,10)
    pygame.draw.rect(screen, RED, buy_button,0,10)
    pygame.draw.rect(screen, LIGHT_BLUE, menu_button,0,10)

    button_text = button_font.render("Comprar +1 recurso", True, (255, 255, 255))
    text_rect = button_text.get_rect(center=buy_button.center)
    screen.blit(button_text, text_rect)

    button_text = button_font.render("Vender +1 recurso", True, (255, 255, 255))
    text_rect = button_text.get_rect(center=sell_button.center)
    screen.blit(button_text, text_rect)

    button_text = button_font.render("Abrir Menú de Recursos", True, (255, 255, 255))
    text_rect = button_text.get_rect(center=menu_button.center)
    screen.blit(button_text, text_rect)
    if button_menu_on == True:
        pygame.draw.rect(screen, LIGHT_BLUE, menu_button_off,0,10)
        button_text = button_font.render("Cerrar Menú de Recursos", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=menu_button_off.center)
        screen.blit(button_text, text_rect)

    if msg:
        msg_text = msg_font.render(msg, True, RED)
        msg_rect = msg_text.get_rect(center=(400, 300))
        screen.blit(msg_text, msg_rect)
    elif msg_sell:
        msg_text = msg_font.render(msg_sell, True, GREEN)
        msg_rect = msg_text.get_rect(center=(400, 300))
        screen.blit(msg_text, msg_rect)
    if open_menu == True:
        pygame.draw.rect(screen, GRAY, menu_resources,0,10)
        y_offset = 130
        resource_title_txt = "Lista de Materiales"
        text_surface = menu_font_title.render(resource_title_txt, True, NEGRO)
        screen.blit(text_surface, (300, 100))
        for resource in resources_list:
            # pygame.draw.rect(screen, GRAY, rect_resources,0,10)
            resource_text = f"[{resource['index']}] - Material: {resource['mat']} - Precio: ${resource['precio']}"
            text_surface = menu_font.render(resource_text, True, NEGRO)
            # txt_rect = text_surface.get_rect(center=rect_resources.center)
            screen.blit(text_surface, (255, y_offset))
            y_offset += 50
        rect_resources = pygame.Rect(100, 400, 240, 50) 
        for resource in resources_list:
            pass

# RECTANGULOS *********************************************
menu_button = pygame.Rect(275,460, 240, 50)
menu_button_off = pygame.Rect(275,460, 240, 50)
sell_button = pygame.Rect(450, 400, 240, 50)  # x, y, ancho, alto
buy_button = pygame.Rect(100, 400, 240, 50) 



menu_resources = pygame.Rect(245, 80, 300, 300) 

# FUENTES ************************************************
menu_font = pygame.font.SysFont(None, 25)
menu_font_title = pygame.font.SysFont(None, 30)
button_font = pygame.font.SysFont(None, 35)
msg_font = pygame.font.SysFont(None, 35)
# MENSAJES CONFIG *****************************************
msg = ""
msg_sell = ""
msg_timer = 0

NEGRO = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
LIGHT_BLUE = (37,150,190)
GRAY = (142, 142, 142, 1)

msg_timer = 0

# MENU CONFIG
open_menu = False
button_menu_on = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición actual del ratón
            if sell_button.collidepoint(mouse_pos):  # Verifica si el click ocurrio dentro del boton
                if resources >0:
                    resources -= 1
                    add_money(100)
                    msg_sell = "¡Recurso Vendido!"  
                    msg_timer = pygame.time.get_ticks()
            elif buy_button.collidepoint(mouse_pos):
                if money >= 90:
                    spend_money(90)
                    add_resources(1)
                    msg = "¡Recurso Comprado!"
                    msg_timer = pygame.time.get_ticks()  # Iniciar temporizador
            elif menu_button.collidepoint(mouse_pos):
                # if event.button == 1: #Click izq
                    menu_button.x = -275
                    button_menu_on = True
                    open_menu = True
                    print(open_menu)
            elif menu_button_off.collidepoint(mouse_pos):
                # if event.button == 3: #click derecho
                    menu_button.x = 275
                    open_menu = False
                    button_menu_on = False
                    print(open_menu)
    if msg or msg_sell:
        timer_actual = pygame.time.get_ticks()
        if timer_actual - msg_timer >= 500: 
            msg = ""
            msg_sell = ""

    screen.blit(fondo,(0,0))
    draw_ui(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
