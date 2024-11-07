from functions import clip_set_to_list_on_xaxis, separate_sets_from_yaxis
from window import window
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
with open(f"{resources_path}/sprites/player.json") as json_file:
    player_data = json.load(json_file)


class Player:
    def __init__(self):
        self.init_images()
        self.init_movement()
        self.init_rect()

        self.idx = 0

    def init_images(self):
        spritesets = pygame.image.load(
            f"{resources_path}/sprites/player.png")
        
        separated_spritesets = separate_sets_from_yaxis(
            spritesets, (255, 0, 0))
        
        self.images = {}
        for name, spriteset in zip(player_data["direction_order"], separated_spritesets):
            sprites = clip_set_to_list_on_xaxis(spriteset)

            self.images[name] = sprites

    def init_movement(self):
        self.vel = 2
        self.direction = "down"
        self.moving = False

    def init_rect(self):
        size = self.images[self.direction][0].get_rect().size
        self.rect = pygame.Rect(player_data["starting_position"], size)

    # Draw
    def draw(self, display):
        images = self.images[self.direction]

        # Reset
        if self.idx >= len(images) * 7:
            self.idx = 0

        # Draw player
        img = images[self.idx // 7]
        display.blit(img, self.rect)

        # Update
        if self.moving:
            self.idx += 1

    # Actions
    def movement(self):
        keys = pygame.key.get_pressed()

        # Left
        if keys[pygame.K_a]:
            self.move_x(-self.vel)
            self.moving = True
            self.direction = "left"
        # Right
        elif keys[pygame.K_d]:
            self.move_x(self.vel)
            self.moving = True
            self.direction = "right"
        # Up
        elif keys[pygame.K_w]:
            self.move_y(-self.vel)
            self.moving = True
            self.direction = "up"
        # Down
        elif keys[pygame.K_s]:
            self.move_y(self.vel)
            self.moving = True
            self.direction = "down"

    def move_x(self, vel):
        self.rect.x += vel

    def move_y(self, vel):
        self.rect.y += vel

    # Update
    def update(self):
        pass