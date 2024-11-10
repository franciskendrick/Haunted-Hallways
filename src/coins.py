from functions import clip_set_to_list_on_xaxis
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


class Coins:
    def __init__(self):
        positions = [
            [29, 2],
            [6, 5],
            [20, 6],
            [38, 7],
            [25, 8],
            [10, 15],
            [23, 20],
            [2, 24],
            [40, 24],
            [12, 25],
            [22, 29],
            [11, 36],
            [21, 38]
        ]

        self.images = clip_set_to_list_on_xaxis(
            pygame.image.load(f"{resources_path}/sprites/coin.png"))
        self.idx = 0
        
        x_offset, y_offset = maze_data["starting_position"]
        self.coin_rect = []
        for (x, y) in positions:
            self.coin_rect.append([pygame.Rect((x * 32) - 32 + x_offset, (y * 32) + y_offset - 16, 32, 32), (x-1, y-1)])
        
    def draw(self, display):
        if self.idx >= len(self.images) * 5:
            self.idx = 0

        for rect, _ in self.coin_rect:
            img = self.images[self.idx // 5]
            display.blit(img, rect)

        self.idx += 1

    def move_x(self, vel):
        for rect, _ in self.coin_rect:
            rect.x -= vel

    def move_y(self, vel):
        for rect, _ in self.coin_rect:
            rect.y -= vel

    def check_collision(self, hitbox):
        pass