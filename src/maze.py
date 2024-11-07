import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)

# Json
with open(f"{resources_path}/maze/maze.json") as json_file:
    maze_data = json.load(json_file)


class Maze:
    # Initialize
    def __init__(self):
        # Images
        self.images = {
            "floor": pygame.image.load(f"{resources_path}/maze/floor.png"),
            "walls1": pygame.image.load(f"{resources_path}/maze/walls1.png"),
            "walls2": pygame.image.load(f"{resources_path}/maze/walls2.png")
        }

        # Rectangle
        size = self.images["floor"].get_rect().size
        self.rect = pygame.Rect(maze_data["starting_position"], size)

    # Draw
    def draw(self, display, name):
        display.blit(self.images[name], self.rect)

    # Action
    def move_x(self, vel):
        self.rect.x -= vel

    def move_y(self, vel):
        self.rect.y -= vel