import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

#imagenes
fondo = pygame.image.load("imagenes/principal/ciudad_bien.png")
icon = pygame.image.load("imagenes/principal/escudo_icon.png")

image_menu = pygame.image.load("imagenes/principal/fabric_menu.jpg")
image_menu = pygame.transform.scale(image_menu, (150, 150))

image_silla = pygame.image.load("imagenes/muebles/silla.png")
image_silla = pygame.transform.scale(image_silla, (110, 110))
image_cama = pygame.image.load("imagenes/muebles/cama.png")
image_cama = pygame.transform.scale(image_cama, (110, 110))
image_mesa = pygame.image.load("imagenes/muebles/mesa.png")
image_mesa = pygame.transform.scale(image_mesa, (110, 110))
image_armario = pygame.image.load("imagenes/muebles/armario.png")
image_armario = pygame.transform.scale(image_armario, (110, 110))

#sonidos 

sound_yes = pygame.mixer.Sound("sounds/buttons/yes1.mp3")
sound_no = pygame.mixer.Sound("sounds/buttons/no1.mp3")
open_1 = pygame.mixer.Sound("sounds/buttons/open1.mp3")
close_1 = pygame.mixer.Sound("sounds/buttons/cerrar1.mp3")
click_1 = pygame.mixer.Sound("sounds/buttons/click1.mp3")

pygame.mixer.music.load("sounds/music/inicio.mp3")
pygame.mixer.music.set_volume(1)  # Reproducir en bucle
pygame.mixer.music.play(-1)  # Reproducir en bucle


pygame.display.set_icon(icon)
pygame.display.set_caption("Tycoon en PyGame")

clock = pygame.time.Clock()

# Variables globales
money = 1000
resources = 0
frabricacion = ""
fabricar = []
resources_list = [
    {"borde":10,"radio": -1,"rect":pygame.Rect(255, 130, 240, 50),"index":1,"mat": "Silla", "precio": 50,},
    {"borde":10,"radio": -1,"rect":pygame.Rect(255, 130, 240, 50),"index":2,"mat": "Mesa", "precio": 100},
    {"borde":10,"radio": -1,"rect":pygame.Rect(255, 130, 240, 50),"index":3,"mat": "Cama", "precio": 70},
    {"borde":10,"radio": -1,"rect":pygame.Rect(255, 130, 240, 50),"index":4,"mat": "Armario", "precio": 150}
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
# Función para dibujar la UI
def draw_interfaz(screen):
    screen.blit(fondo,(0,0))
    if open_main_menu == True:
        draw_rect(screen, main_menu_rect, "TYCOON EN PYGAME", NEGRO,menu_font_title, GREEN, (400,100))
        draw_button(screen, play_button, "JUGAR", NEGRO, LIGHT_BLUE, mouse_pos)
        draw_button(screen, close_button, "CERRAR", NEGRO, RED, mouse_pos)
        screen.blit(image_menu,(325,130))
    else:
        if estadisticas_on == True:
            font = pygame.font.SysFont(None, 50)
            money_text = font.render(f"Dinero: ${money}", True, NEGRO)
            resources_text = font.render(f"Recursos: {resources}", True, NEGRO)
            screen.blit(money_text, (40, 70))
            screen.blit(resources_text, (40, 100))

        draw_button(screen, sell_button, "Vender +1 recurso", NEGRO, GREEN, mouse_pos)
        draw_button(screen, buy_button, "Comprar +1 recurso", NEGRO, RED, mouse_pos)
        draw_button(screen, menu_button, "Menú de Fabricación", NEGRO, GRAY, mouse_pos)

        if button_menu_resources_rect_on == True:
            draw_button(screen, menu_button_off, "Cerrar Menú de Fabricación", NEGRO, GRAY, mouse_pos)
        if estadisticas_on == True:
            draw_button(screen, estadistica_button_off, "Ocultar Estadisticas", NEGRO, LIGHT_BLUE, mouse_pos)
        else:
            draw_button(screen, estadistica_button, "Mostrar Estadisticas", NEGRO, LIGHT_BLUE, mouse_pos)

        if msg:
            msg_text = msg_font.render(msg, True, RED)
            msg_rect = msg_text.get_rect(center=(400, 300))
            screen.blit(msg_text, msg_rect)
        elif msg_sell:
            msg_text = msg_font.render(msg_sell, True, GREEN)
            msg_rect = msg_text.get_rect(center=(400, 300))
            screen.blit(msg_text, msg_rect)
resource_rects = []

# Crear los rectángulos basados en la lista de recursos
def new_rect():
    global resource_rects
    resource_rects = []
    espacio_y = 130
    for resource in resources_list:
        resource = pygame.Rect(250, espacio_y, 300, 40)  # Crear un rectángulo para cada recurso
        resource_rects.append(resource)
        espacio_y += 50

new_rect() # ya creo los rect
def draw_menu_resources(screen):
    if open_main_menu == False:
        if open_menu_resources_rect == True:
            pygame.draw.rect(screen, GRAY, menu_resources_rect, 0, 10)
            draw_button(screen, fabric_1_button, "[1]", NEGRO, BLANCO, mouse_pos)
            draw_button(screen, fabric_2_button, "[2]", NEGRO, BLANCO, mouse_pos)
            draw_button(screen, fabric_3_button, "[3]", NEGRO, BLANCO, mouse_pos)
            draw_button(screen, fabric_4_button, "[4]", NEGRO, BLANCO, mouse_pos)
            y_offset = 150
            resource_title_txt = "Lista de Fabricación"
            text_surface = menu_font_title.render(resource_title_txt, True, NEGRO)
            screen.blit(text_surface, (300, 100))
            for resource in resources_list:
                resource_text = f"[{resource['index']}] {resource['mat']} - Precio: ${resource['precio']}"
                text_surface = menu_font.render(resource_text, True, NEGRO)
                screen.blit(text_surface, (300, y_offset))
                y_offset += 50
            is_dialog_on(screen)
            # if dialog_on == True:
            #     draw_rect(screen, dialog_yes_no_rect, "¿Fabricar este mueble?", NEGRO,menu_font_title, BLANCO, (400,100))
            #     draw_button(screen, dialog_yes_button, "SI", NEGRO, GREEN, mouse_pos)
            #     draw_button(screen, dialog_no_button, "NO", NEGRO, RED, mouse_pos)
            #     if silla == True:
            #         screen.blit(image_silla,(345,140))

def is_dialog_on(screen):
    if dialog_on == True:
        draw_rect(screen, dialog_yes_no_rect, "¿Fabricar este mueble?", NEGRO,menu_font_title, BLANCO, (400,100))
        draw_button(screen, dialog_yes_button, "SI", NEGRO, GREEN, mouse_pos)
        draw_button(screen, dialog_no_button, "NO", NEGRO, RED, mouse_pos)
        if silla == True:
            screen.blit(image_silla,(345,140))
        if mesa == True:
            screen.blit(image_mesa,(345,140))
        if cama == True:
            screen.blit(image_cama,(345,140))
        if armario == True:
            screen.blit(image_armario,(345,140))

def draw_button(screen, rect, text, text_color, rect_color, mouse_pos):
    # Crear una copia del rectángulo para inflarlo temporalmente
    temp_rect = rect.copy()
    if temp_rect.collidepoint(mouse_pos):
        temp_rect.inflate_ip(10, 10)

    pygame.draw.rect(screen, rect_color, temp_rect, 0, 10)
    text_surface = button_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=temp_rect.center)
    screen.blit(text_surface, text_rect)

def draw_rect(screen, rect, text, text_color, font, rect_color, rect_center:tuple):

    pygame.draw.rect(screen, rect_color, rect, 0, 10)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect_center)
    screen.blit(text_surface, text_rect)

def create_text(text, font, color, pos):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)
    screen.blit(text_surface, text_rect)





# RECTANGULOS BOTONES *********************************************
# menu recursos
menu_button = pygame.Rect(275,460, 240, 50)
menu_button_off = pygame.Rect(240,460, 320, 50)

fabric_1_button = pygame.Rect(245,345, 50, 50)
fabric_2_button = pygame.Rect(320,345, 50, 50)
fabric_3_button = pygame.Rect(420,345, 50, 50)
fabric_4_button = pygame.Rect(495,345, 50, 50)

dialog_yes_no_rect = pygame.Rect(274,90, 250, 250)

dialog_yes_button  = pygame.Rect(290,245, 50, 50)
dialog_no_button  = pygame.Rect(460,245, 50, 50)


# vender y comprar
sell_button = pygame.Rect(450, 400, 240, 50)  # x, y, ancho, alto
buy_button = pygame.Rect(100, 400, 240, 50) 
# estadisticas
estadistica_button = pygame.Rect(30, 10, 240, 50)
estadistica_button_off = pygame.Rect(30, 10, 240, 50)
# main menu
play_button = pygame.Rect(280, 300, 240, 50)
close_button = pygame.Rect(280,400, 240, 50)


# RECTANGULOS MENU RECURSOS *********************************************
menu_resources_rect = pygame.Rect(245, 80, 300, 300) 
# RECTANGULOS MAIN MENU *********************************************
main_menu_rect = pygame.Rect(250, 70, 300, 400) 
# FUENTES ************************************************
quest_font = pygame.font.SysFont(None, 25)
menu_font = pygame.font.SysFont(None, 25)
menu_font_title = pygame.font.SysFont(None, 30)
button_font = pygame.font.SysFont(None, 35)
Title_font = pygame.font.SysFont(None, 50)
msg_font = pygame.font.SysFont(None, 35)
# MENSAJES CONFIG *****************************************
msg = ""
msg_sell = ""
msg_timer = 0
# COLORES *********************************************
BLANCO = (255,255,255)
NEGRO = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
LIGHT_BLUE = (37,150,190)
GRAY = (142, 142, 142, 1)
# MENU RECURSOS CONFIG *********************************************
dialog_on = False
silla = False
mesa = False
cama = False
armario = False
open_menu_resources_rect = False
button_menu_resources_rect_on = False
# MAIN MENU CONFIG *********************************************
open_main_menu = True
esc_press = False
# ESTADISTICAS CONFIG **************************************
estadisticas_on = True
# EL MALDITO BUCLE *********************************************
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición actual del ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # COMPRAR
            if sell_button.collidepoint(mouse_pos):  # Verifica si el click ocurrio dentro del boton
                if resources >0:
                    resources -= 1
                    add_money(100)
                    msg_sell = "¡Recurso Vendido!"  
                    msg_timer = pygame.time.get_ticks()
            # VENDER
            elif buy_button.collidepoint(mouse_pos):
                if money >= 90:
                    spend_money(90)
                    add_resources(1)
                    msg = "¡Recurso Comprado!"
                    msg_timer = pygame.time.get_ticks()
            # ABRIR MENU RECURSOS
            elif menu_button.collidepoint(mouse_pos):
                # if event.button == 1: #Click izq
                open_1.play()
                menu_button.x = -275
                open_menu_resources_rect = True
                button_menu_resources_rect_on = True
                    
            # CERRAR MENU RECURSOS
            elif menu_button_off.collidepoint(mouse_pos):
                # if event.button == 3: #click derecho
                close_1.play()
                menu_button.x = 275
                open_menu_resources_rect = False
                button_menu_resources_rect_on = False

            elif fabric_1_button.collidepoint(mouse_pos):
                click_1.play()
                dialog_on = True
                silla = True
            elif dialog_yes_button.collidepoint(mouse_pos):
                sound_yes.play()
                if silla:
                    spend_money(50)
                    add_resources(1)
                dialog_on = False
                silla = False
            elif dialog_no_button.collidepoint(mouse_pos):
                sound_no.play()
                dialog_on = False
                silla = False
            elif fabric_2_button.collidepoint(mouse_pos):
                click_1.play()
                dialog_on = True
                mesa = True
            elif dialog_yes_button.collidepoint(mouse_pos):
                sound_yes.play()
                if mesa:
                    spend_money(100)
                    add_resources(1)
                dialog_on = False
                mesa = False
            elif dialog_no_button.collidepoint(mouse_pos):
                sound_no.play()
                dialog_on = False
                mesa = False
            elif fabric_3_button.collidepoint(mouse_pos):
                click_1.play()
                dialog_on = True
                cama = True
            elif dialog_yes_button.collidepoint(mouse_pos):
                sound_yes.play()
                if cama:
                    spend_money(70)
                    add_resources(1)
                dialog_on = False
                cama = False
            elif dialog_no_button.collidepoint(mouse_pos):
                sound_no.play()
                dialog_on = False
                cama = False
            elif fabric_4_button.collidepoint(mouse_pos):
                click_1.play()
                dialog_on = True
                armario = True
            elif dialog_yes_button.collidepoint(mouse_pos):
                sound_yes.play()
                if armario:
                    spend_money(150)
                    add_resources(1)
                dialog_on = False
                armario = False
            elif dialog_no_button.collidepoint(mouse_pos):
                sound_no.play()
                dialog_on = False
                armario = False
            # CERRAR y ABRIR ESTADISTICAS
            elif estadistica_button_off.collidepoint(mouse_pos):
                estadistica_button_off.x = -300 
                estadisticas_on = False
            elif estadistica_button.collidepoint(mouse_pos):
                estadisticas_on = True
                estadistica_button_off.x = 30 
        # CERRAR y ABRIR MENU
            elif play_button.collidepoint(mouse_pos):
                open_main_menu = False
                click_1.play()
            elif close_button.collidepoint(mouse_pos):
                running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                open_main_menu = True   




    if msg or msg_sell:
        timer_actual = pygame.time.get_ticks()
        if timer_actual - msg_timer >= 500: 
            msg = ""
            msg_sell = ""

    screen.blit(fondo,(0,0))
    draw_interfaz(screen)
    draw_menu_resources(screen)
    # if open_main_menu == False: 
        # if silla == True:
            # create_text("(Silla)",quest_font,NEGRO,(375,110))
            # screen.blit(image_silla,(345,140))
        # if mesa == True:    
        #     create_text("(Mesa)",quest_font,NEGRO,(375,110))
        # if cama == True:    
        #     create_text("(Cama)",quest_font,NEGRO,(375,110))
        # if armario == True:    
        #     create_text("(Armario)",quest_font,NEGRO,(375,110))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
