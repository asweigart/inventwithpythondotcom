# Basic Pygame setup stuff:
import pygame, sys, time
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP

pygame.init()  # Initialize the Pygame library.
BG_COLOR = (0, 255, 220)  # The RGB color for the background.
DISPLAY_SURF = pygame.display.set_mode((600, 600))  # Create a 600x600 window.
fps_clock = pygame.time.Clock()  # Frames-per-second timer.

# Get the cat image and set its position:
cat_surface = pygame.Surface((80, 80))
cat_surface.fill((250, 0, 130))  # Use a pink 80x80 square for the "cat"
# If you don't have a cat.png file, comment out this line:
cat_surface = pygame.image.load('cat.png')  # Use a cat image for the cat sprite.
cat_rect = cat_surface.get_rect()
cat_rect.left = 50  # Set left edge of cat sprite at X coordinate 50.
cat_rect.top = 100  # Set top edge of cat sprite at Y coordinate 100.

# Draw the cat and pause for a couple seconds:
DISPLAY_SURF.fill(BG_COLOR)  # Clear the window.
DISPLAY_SURF.blit(cat_surface, cat_rect)  # Draw the cat.
pygame.display.update()  # Render the screen.
pygame.event.get()  # Required on macOS to display the window, for some reason.
time.sleep(2)

debug_output = True
print('DEBUG\tLEFT\tTOP')  # DEBUG OUTPUT
while True:
    # Terminate when the user closes the window or presses a key.
    for event in pygame.event.get():  # Event handling loop.
        if event.type in (QUIT, KEYUP, MOUSEBUTTONUP):
            pygame.quit()
            sys.exit()

    if cat_rect.left < 400:
        # Move the cat to the right by 10 pixels:
        cat_rect.left += 10
        if debug_output:
            print('DEBUG\t', cat_rect.left, '\t', cat_rect.top)  # DEBUG OUTPUT
    else:
        time.sleep(1)  # Pause for a second after the animation is done. (User can't quit during this second. No biggie though.)
        cat_rect.left = 50  # Reset the cat to the start.
        debug_output = False  # Only show debug output for the first movement, then disable it.

    DISPLAY_SURF.fill(BG_COLOR)  # Clear the window.
    DISPLAY_SURF.blit(cat_surface, cat_rect)  # Draw the cat.
    pygame.display.update()  # Render the screen.
    fps_clock.tick(30)  # Run at 30 frames per second.
