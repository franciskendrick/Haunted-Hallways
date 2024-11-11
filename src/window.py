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

        # Flashlight
        self.init_vignette()

        # You Won
        self.youwon_image = pygame.image.load(
            f"{resources_path}/screens/youwon.png")

    def init_vignette(self):
        self.radius = 150
        self.mask = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.mask.fill((0, 0, 0, 240))

    def draw_flashlight(self, display, center):
        #
        pygame.draw.circle(
            self.mask, (9, 10, 20, 0), center, self.radius)
        
        display.blit(self.mask, (0, 0))

    def draw_youwon(self, display):
        display.blit(self.youwon_image, (175, 90))



window = Window()