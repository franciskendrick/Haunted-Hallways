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
        self.init()
        self.init_mazegrid()

    def init(self):
        # Images
        self.images = {
            "floor": pygame.image.load(f"{resources_path}/maze/floor.png"),
            "walls1": pygame.image.load(f"{resources_path}/maze/walls1.png"),
            "walls2": pygame.image.load(f"{resources_path}/maze/walls2.png")
        }

        # Rectangle
        size = self.images["floor"].get_rect().size
        self.rect = pygame.Rect(maze_data["starting_position"], size)

    def init_mazegrid(self):
        # Maze Grid
        self.maze_grid = maze_data["maze_grid"]
        start_x, start_y = maze_data["starting_position"]
        self.rect_grid = [[[pygame.Rect((x * 32) + start_x, (y * 32) + start_y + 16, 32, 32), cell] 
                           for x, cell in enumerate(rows)] for y, rows in enumerate(self.maze_grid)]
        
        self.floor_rects = []
        for y, row in enumerate(self.rect_grid):
            for x, (maze_rect, cell_type) in enumerate(row):
                if cell_type == 0:
                    self.floor_rects.append([maze_rect, (x, y)])

    # Draw
    def draw(self, display, name):
        display.blit(self.images[name], self.rect)

    def draw_rect(self, display):
        for row in self.rect_grid:
            for (rect, cell) in row:
                color = (128, 0, 0) if cell == 1 else (255, 255, 255)
                pygame.draw.rect(display, color, rect)

        pygame.draw.rect(display, (0, 255, 0), self.rect, 5)

    # Collision
    def check_collision(self, hitbox):
        for floor_data in self.floor_rects:
            maze_rect, _ = floor_data
            if (hitbox.centerx >= maze_rect.left and hitbox.centerx <= maze_rect.right) and (hitbox.centery >= maze_rect.top and hitbox.centery <= maze_rect.bottom):
                self.prev_floordata = floor_data
                return floor_data

    # Action
    def move_x(self, vel):
        for row in self.rect_grid:
            for (rect, _) in row:
                rect.x -= vel

        self.rect.x -= vel

    def move_y(self, vel):
        for row in self.rect_grid:
            for (rect, _) in row:
                rect.y -= vel

        self.rect.y -= vel