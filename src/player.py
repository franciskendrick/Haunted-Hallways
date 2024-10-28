from window import window
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Player:
    def __init__(self):
        pass

    # Draw
    def draw(self, display):
        pass

    # Actions
    def move(self):
        pass

    # Update
    def update(self):
        pass