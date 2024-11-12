from window import window
from maze import Maze
from player import Player
from coins import Coins
import pygame
import sys


# Redraw
def redraw_game():
    display.fill((0, 0, 0))

    if status == "playing" or status == "menu":
        # Draw entities
        maze.draw(display, "floor")
        maze.draw(display, "walls1")
        coins.draw(display)
        player.draw(display)
        maze.draw(display, "walls2")

        # Draw flashlight effect
        window.draw_flashlight(display, player.rect.center)
    elif status == "win":
        player.draw(display)
        window.draw_youwon(display)
    elif status == "lost":
        window.draw_jumpscare(display)  # Assuming you have a "You Lost" screen

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loops
def game_loop():
    global status, start_time

    run = True
    last_print_time = 0  # Track the last time the status was printed

    while run:
        # Check game events
        for event in pygame.event.get():
            # Check if user closed the game window
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYUP:
                player.moving = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and status == "menu":
                    status = "playing"
                    start_time = pygame.time.get_ticks()  # Start timer
                    last_print_time = start_time  # Reset print timer
                if event.key == pygame.K_SPACE and status == "lost":
                    status = "menu"
                    maze.init()
                    player.init_images()
                    player.init_movement()
                    player.init_rect()
                    coins.init()

        # Update game logic
        if status == "playing":
            player.movement(maze, coins)

            # Check if player collected all coins
            if len(coins.coin_rects) <= 0:
                status = "win"

            # Check for timer expiration
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time >= 360000:  # 360000 ms = 6 minutes
                status = "lost"

            # Print remaining time and coins every second
            current_time = pygame.time.get_ticks()
            if current_time - last_print_time >= 1000:  # 1000 ms = 1 second
                remaining_time_sec = (360000 - elapsed_time) // 1000
                minutes = remaining_time_sec // 60
                seconds = remaining_time_sec % 60
                remaining_coins = len(coins.coin_rects)

                print(f"{minutes:02}:{seconds:02} | Remaining Coins: {remaining_coins}")
                last_print_time = current_time  # Update the last print time

        # Redraw
        redraw_game()

        # Framerate
        clock.tick(window.framerate)

    # Exit program
    pygame.quit()
    sys.exit()


# Execute
if __name__ == "__main__":
    pygame.init()

    # Initialize entities
    maze = Maze()
    player = Player()
    coins = Coins()

    status = "menu"
    start_time = 0  # Initialize start time

    # Initialize pygame window
    win_size = (
        int(window.rect.width * window.enlarge),
        int(window.rect.height * window.enlarge))
    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(window.rect.size)
    pygame.display.set_caption("Haunted Hallways")
    clock = pygame.time.Clock()

    # Run the game
    game_loop()
