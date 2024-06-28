import pygame
from settings import *
from main_god import *


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
        draw_rect(screen, main_menu_rect, "TYCOON EN ROBLOX", NEGRO,menu_font_title, GREEN, (400,100))
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
        if dialog_on == True:
            draw_rect(screen, dialog_yes_no_rect, "¿Fabricar este mueble?", NEGRO,menu_font_title, BLANCO, (400,100))
            draw_button(screen, dialog_yes_button, "SI", NEGRO, GREEN, mouse_pos)
            draw_button(screen, dialog_no_button, "NO", NEGRO, RED, mouse_pos)

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

def new_rect():
    global resource_rects
    resource_rects = []
    espacio_y = 130
    for resource in resources_list:
        resource = pygame.Rect(250, espacio_y, 300, 40)  # Crear un rectángulo para cada recurso
        resource_rects.append(resource)
        espacio_y += 50