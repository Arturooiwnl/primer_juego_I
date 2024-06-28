import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla y colores
ANCHO, ALTO = 1000, 600
SCREEN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento en diagonal con rebote")
RED = (255, 0, 0)
FPS = 60
clock = pygame.time.Clock()

# Configuración del rectángulo
rect_1 = pygame.Rect(50, 50, 200, 100)
speed_x, speed_y = 5, 5

# Cargar la imagen
image = pygame.image.load("imagenes/escudo_icon.png")  # Reemplaza 'ruta/a/tu/imagen.png' con la ruta a tu imagen
image = pygame.transform.scale(image, (50, 50))  # Escalar la imagen al tamaño deseado

# Variables de control
is_running = True

while is_running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Mover el rectángulo
    rect_1.x += speed_x
    rect_1.y += speed_y

    # Detectar colisiones con los bordes de la pantalla y cambiar la dirección
    if rect_1.left <= 0 or rect_1.right >= ANCHO:
        speed_x = -speed_x
    if rect_1.top <= 0 or rect_1.bottom >= ALTO:
        speed_y = -speed_y

    # Dibujar en la pantalla
    SCREEN.fill((0, 0, 0))  # Limpiar la pantalla con color negro

    # Dibujar el rectángulo
    # pygame.draw.rect(SCREEN, RED, rect_1)

    # Calcular el centro del rectángulo y dibujar el círculo
    center_x = rect_1.centerx
    center_y = rect_1.centery
    radius = 50  # Puedes ajustar el radio según necesites
    # pygame.draw.circle(SCREEN, RED, (center_x, center_y), radius)

    # Calcular la posición de la imagen para centrarla en el círculo
    image_rect = image.get_rect(center=(center_x, center_y))
    SCREEN.blit(image, image_rect.topleft)

    pygame.display.flip()

pygame.quit()
sys.exit()
