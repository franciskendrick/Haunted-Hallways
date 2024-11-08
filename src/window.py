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
        self.enlarge = 2  # temporary !!!

        # Framerate
        self.framerate = 60


window = Window()