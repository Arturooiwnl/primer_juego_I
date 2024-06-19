import pygame

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.Font(font, 32)
        self.change_text(text, bg)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, True, pygame.Color("white"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.change_text(self.feedback, bg="red")
            return True
        return False

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))

# Crear un botón
button = Button("Click me", (350, 250), None, bg="navy", feedback="You clicked!")

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.click(event):
                print("Button clicked!")

    # Llenar la pantalla de negro
    screen.fill((0, 0, 0))

    # Mostrar el botón
    button.show(screen)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
