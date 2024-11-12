from functions import clip_set_to_list_on_xaxis, separate_sets_from_yaxis
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
    # Initialize
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

        x_offset, y_offset = player_data["hitbox_offset"]
        self.hitbox = pygame.Rect((self.rect.x + x_offset, self.rect.y + y_offset), player_data["hitbox_size"])

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
    def movement(self, maze, coins):
        keys = pygame.key.get_pressed()

        #
        collision_data = maze.check_collision(self.hitbox)

        if collision_data != None:
            collided_cell, (x, y) = collision_data
            left = collided_cell.left > self.hitbox.left
            right = collided_cell.right < self.hitbox.right
            top = collided_cell.top > self.hitbox.top
            bottom = collided_cell.bottom < self.hitbox.bottom

            # Left
            if keys[pygame.K_a] and not (left and maze.rect_grid[y][x-1][1]):
                maze.move_x(-self.vel)
                coins.move_x(-self.vel)
                self.moving = True
                self.direction = "left"

            # Right
            elif keys[pygame.K_d] and not (right and maze.rect_grid[y][x+1][1]):
                maze.move_x(self.vel)
                coins.move_x(self.vel)
                self.moving = True
                self.direction = "right"

            # Up
            if keys[pygame.K_w] and not (top and maze.rect_grid[y-1][x][1]):
                maze.move_y(-self.vel)
                coins.move_y(-self.vel)
                self.moving = True
                self.direction = "up"

            # Down
            elif keys[pygame.K_s] and not (bottom and y != 40 and maze.rect_grid[y+1][x][1] == 1):
                maze.move_y(self.vel)
                coins.move_y(self.vel)
                self.moving = True
                self.direction = "down"
        else:
            _, (x, y) = maze.prev_floordata
            maze.rect.x = x - 387 - 20
            maze.rect.y = y - 1027 - 40
            maze.init_mazegrid()
            coins.update_rect()

        #
        coins.check_collision(self.hitbox)
