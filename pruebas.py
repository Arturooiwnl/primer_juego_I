import pygame

for color in pygame.color.THECOLORS.keys():
    print(color)
for value in pygame.color.THECOLORS.values():
    print(value)
for key, value in pygame.color.THECOLORS.items():
    print(key, value)

rect_1 = pygame.Rect()

# rect_2 = (x,y,ancho,alto)