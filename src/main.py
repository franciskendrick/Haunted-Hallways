from window import window
from player import Player
import pygame
import sys


# Redraw
def redraw_game():
    # Draw entities
    player.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loops
def game_loop():
    run = True
    while run:
        # Check game events
        for event in pygame.event.get():
            # Check if user closed the game window
            if event.type == pygame.QUIT:
                run = False

        

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
    player = Player()    

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