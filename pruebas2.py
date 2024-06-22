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
    {"index": 1, "mat": "Madera", "precio": 20},
    {"index": 2, "mat": "Piedra", "precio": 30},
    {"index": 3, "mat": "Agua", "precio": 15},
    {"index": 4, "mat": "Metal", "precio": 50}
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

# Crear rectángulos para los recursos
def new_rect():
    global resource_rects
    resource_rects = []
    espacio_y = 130
    for resource in resources_list:
        rect = pygame.Rect(250, espacio_y, 300, 40)  # Crear un rectángulo para cada recurso
        resource_rects.append(rect)
        espacio_y += 50

new_rect()

# Función para dibujar el menú de recursos
def draw_menu(screen, mouse_pos):
    if open_menu_resources_rect:
        pygame.draw.rect(screen, GRAY, menu_resources_rect, 0, 10)
        resource_title_txt = "Lista de Fabricación"
        text_surface = menu_font_title.render(resource_title_txt, True, NEGRO)
        screen.blit(text_surface, (300, 100))
        for i in range(len(resources_list)):
            resource = resources_list[i]
            rect = resource_rects[i]
            resource_text = f"[{resource['index']}] {resource['mat']} - Precio: ${resource['precio']}"
            draw_button(screen, rect, resource_text, NEGRO, BLANCO, mouse_pos)

# Función para dibujar botones con efecto de agrandamiento
def draw_button(screen, rect, text, text_color, rect_color, mouse_pos):
    temp_rect = rect.copy()
    if temp_rect.collidepoint(mouse_pos):
        temp_rect.inflate_ip(10, 10)
        pygame.draw.rect(screen, (0, 0, 0), temp_rect, 3)  # Dibuja el borde en negro
    pygame.draw.rect(screen, rect_color, temp_rect, 0, 5)
    text_surface = menu_font.render(text, True, text_color)
    screen.blit(text_surface, (temp_rect.x + 6, temp_rect.y + 6))

# Función para dibujar la UI
def draw_ui(screen, mouse_pos):
    font = pygame.font.SysFont(None, 50)
    money_text = font.render(f"Dinero: ${money}", True, NEGRO)
    resources_text = font.render(f"Recursos: {resources}", True, NEGRO)
    screen.blit(money_text, (10, 10))
    screen.blit(resources_text, (10, 40))
    draw_button(screen, sell_button, "Vender +1 recurso", BLANCO, RED, mouse_pos)
    draw_button(screen, buy_button, "Comprar +1 recurso", BLANCO, GREEN, mouse_pos)
    draw_button(screen, menu_button, "Menú de Recursos", BLANCO, GRAY, mouse_pos)

# Función para dibujar el cuadro de diálogo
def draw_dialog(screen, text, yes_button, no_button, mouse_pos):
    pygame.draw.rect(screen, GRAY, dialog_rect)
    dialog_text_surface = menu_font.render(text, True, NEGRO)
    screen.blit(dialog_text_surface, (dialog_rect.x + 20, dialog_rect.y + 20))
    draw_button(screen, yes_button, "Sí", BLANCO, GREEN, mouse_pos)
    draw_button(screen, no_button, "No", BLANCO, RED, mouse_pos)

# RECTANGULOS *********************************************
menu_button = pygame.Rect(275, 460, 240, 50)
sell_button = pygame.Rect(450, 400, 240, 50)  # x, y, ancho, alto
buy_button = pygame.Rect(100, 400, 240, 50) 
menu_resources_rect = pygame.Rect(250, 80, 300, 400)
dialog_rect = pygame.Rect(200, 200, 400, 200)
yes_button = pygame.Rect(270, 300, 100, 50)
no_button = pygame.Rect(430, 300, 100, 50)

# FUENTES ************************************************
button_font = pygame.font.SysFont(None, 35)
menu_font = pygame.font.SysFont(None, 25)
menu_font_title = pygame.font.SysFont(None, 30)
msg_font = pygame.font.SysFont(None, 35)

# MENSAJES CONFIG *****************************************
msg = ""
msg_sell = ""
msg_timer = 0

NEGRO = (0,0,0)
BLANCO = (255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)
GRAY = (37,150,190)

msg_timer = 0

# MENU CONFIG
open_menu_resources_rect = False
show_dialog = False
current_resource = None

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if sell_button.collidepoint(mouse_pos):
                if resources > 0:
                    remove_resources(1)
                    add_money(100)
                    msg_sell = "¡Recurso Vendido!"
                    msg_timer = pygame.time.get_ticks()
            elif buy_button.collidepoint(mouse_pos):
                if money >= 90:
                    spend_money(90)
                    add_resources(1)
                    msg = "¡Recurso Comprado!"
                    msg_timer = pygame.time.get_ticks()
            elif menu_button.collidepoint(mouse_pos):
                open_menu_resources_rect = True
            elif open_menu_resources_rect:
                for i in range(len(resource_rects)):
                    if resource_rects[i].collidepoint(mouse_pos):
                        show_dialog = True
                        current_resource = resources_list[i]
                        break
                    elif show_dialog == True:
                        draw_dialog(screen, "¿Fabricar?", yes_button, no_button, mouse_pos)
                        if yes_button.collidepoint(mouse_pos):
                            spend_money(current_resource["precio"])
                            add_resources(1)
                            show_dialog = False
                        elif no_button.collidepoint(mouse_pos):
                            show_dialog = False

    if msg or msg_sell:
        timer_actual = pygame.time.get_ticks()
        if timer_actual - msg_timer >= 500:
            msg = ""
            msg_sell = ""

    screen.blit(fondo, (0, 0))
    draw_ui(screen, mouse_pos)
    draw_menu(screen, mouse_pos)
    # if show_dialog == True:
        # draw_dialog(screen, "¿Fabricar?", yes_button, no_button, mouse_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
