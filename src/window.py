import pygame
import os


pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Window:
    def __init__(self):
        # Window
        self.rect = pygame.Rect(0, 0, 540, 540)
        self.enlarge = 1.75  # temporary !!!

        # Framerate
        self.framerate = 60

        self.init_vignette()

    def init_vignette(self):
        self.radius = 150
        self.mask = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.mask.fill((0, 0, 0, 240))

    def draw(self, display, center):
        pygame.draw.circle(
            self.mask, (9, 10, 20, 0), center, self.radius)
        
        display.blit(self.mask, (0, 0))


window = Window()