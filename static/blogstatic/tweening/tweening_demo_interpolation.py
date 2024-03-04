# You can try changing the start/end positions:
START_X, START_Y = 50, 100
END_X, END_Y = 370, 250


# Basic Pygame setup stuff:
import pygame, sys, time, random
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP

pygame.init()  # Initialize the Pygame library.
BG_COLOR = (0, 255, 220)  # The RGB color for the background.
DISPLAY_SURF = pygame.display.set_mode((600, 600))  # Create a 600x600 window.
fps_clock = pygame.time.Clock()  # Frames-per-second timer.

# Get the cat image and set its position:
cat_surface = pygame.Surface((80, 80))
cat_surface.fill((250, 0, 130))  # Use a pink 80x80 square for the "cat"
# If you don't have a cat.png file, comment out this line:
cat_surface = pygame.image.load('cat.png')
cat_rect = cat_surface.get_rect()
cat_rect.left = START_X
cat_rect.top = START_Y
i = 0.0  # The interpolation factor starts at 0.0.

# Draw the cat and pause for a second:
DISPLAY_SURF.fill(BG_COLOR)  # Clear the window.
pygame.draw.rect(DISPLAY_SURF, (255, 255, 255), (START_X, START_Y, cat_rect.width, cat_rect.height))  # Draw white rectangle at start.
pygame.draw.rect(DISPLAY_SURF, (0, 0, 0), (END_X, END_Y, cat_rect.width, cat_rect.height))  # Draw black rectangle at end.
DISPLAY_SURF.blit(cat_surface, cat_rect)  # Draw the cat.
pygame.display.update()  # Render the screen.
pygame.event.get()  # Required on macOS to display the window, for some reason.
time.sleep(1)  # Pause at the start before moving.

debug_output = True
print('DEBUG\ti\tLEFT\tTOP')  # DEBUG OUTPUT
while True:
    # Terminate when the user closes the window or presses a key.
    for event in pygame.event.get():  # Event handling loop.
        if event.type in (QUIT, KEYUP, MOUSEBUTTONUP):
            pygame.quit()
            sys.exit()

    if round(i, 5) <= 1.0:  # round() here is necessary for a weird float rounding issue.
        # Set cat position based on the interpolation factor.
        cat_rect.left = START_X + (i * (END_X - START_X))
        cat_rect.top = START_Y + (i * (END_Y - START_Y))
        if debug_output:
            print('DEBUG\t', round(i, 3), '\t', cat_rect.left, '\t', cat_rect.top)  # DEBUG OUTPUT

        i += 0.02  # Increase the interpolation factor.
    else:
        time.sleep(1)  # Pause for a second after the animation is done. (User can't quit during this second. No biggie though.)
        i = 0.0  # Reset the interpolation factor to 0.0.
        debug_output = False

        # Uncomment the following to randomly change the start & stop positions:
        # START_X = random.randint(0, 600 - cat_rect.width)
        # START_Y = random.randint(0, 600 - cat_rect.height)
        # END_X = random.randint(0, 600 - cat_rect.width)
        # END_Y = random.randint(0, 600 - cat_rect.height)

    DISPLAY_SURF.fill(BG_COLOR)  # Clear the window.
    pygame.draw.rect(DISPLAY_SURF, (255, 255, 255), (START_X, START_Y, cat_rect.width, cat_rect.height))  # Draw white rectangle at start.
    pygame.draw.rect(DISPLAY_SURF, (0, 0, 0), (END_X, END_Y, cat_rect.width, cat_rect.height))  # Draw black rectangle at end.
    DISPLAY_SURF.blit(cat_surface, cat_rect)  # Draw the cat.
    pygame.display.update()  # Render the screen.
    fps_clock.tick(30)  # Run at 30 frames per second.
