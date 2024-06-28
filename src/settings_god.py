import pygame

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("imagenes/principal/ciudad_bien.png")
icon = pygame.image.load("imagenes/principal/escudo_icon.png")
image_menu = pygame.image.load("imagenes/principal/fabric_menu.jpg")
image_menu = pygame.transform.scale(image_menu, (150, 150))

image_silla = pygame.image.load("imagenes/muebles/silla.png")
image_silla = pygame.transform.scale(image_silla, (110, 110))



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