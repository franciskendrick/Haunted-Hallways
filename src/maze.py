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

        # Maze Grid
        self.maze_grid = maze_data["maze_grid"]
        start_x, start_y = maze_data["starting_position"]
        self.rect_grid = [[[pygame.Rect((x * 10), (y * 10), 10, 10), cell] 
                           for x, cell in enumerate(rows)] for y, rows in enumerate(self.maze_grid)]

    # Draw
    # def draw(self, display, name):
    #     display.blit(self.images[name], self.rect)

    def draw(self, display):
        for row in self.rect_grid:
            for (rect, cell) in row:
                color = (128, 0, 0) if cell == 1 else (255, 255, 255)
                pygame.draw.rect(display, color, rect)

    # Action
    def move_x(self, vel):
        for row in self.rect_grid:
            for (rect, _) in row:
                rect.x -= vel

        # self.rect.x -= vel

    def move_y(self, vel):
        for row in self.rect_grid:
            for (rect, _) in row:
                rect.y -= vel

        # self.rect.y -= vel