import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))

# Configurar el texto
font = pygame.font.Font(None, 74)  # Puedes usar una fuente específica pasando la ruta del archivo de fuente
text = font.render('Hola, Pygame!', True, (255, 255, 255))

# Posición del texto
text_rect = text.get_rect(center=(400, 300))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Llenar la pantalla de negro
    screen.fill((0, 0, 0))

    # Dibujar el texto en la pantalla
    screen.blit(text, text_rect)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()


