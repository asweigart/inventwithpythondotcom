import pytweening

# Try changing the various tween functions here:
TWEENS = [pytweening.linear, pytweening.easeOutQuad, pytweening.easeInQuad, pytweening.easeInOutQuad, pytweening.easeOutBounce, pytweening.easeInOutElastic]


# Basic Pygame setup stuff:
import pygame, sys, time, random
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP, MOUSEMOTION

pygame.init()  # Initialize the Pygame library.
BG_COLOR = (0, 255, 220)  # The RGB color for the background.
DISPLAY_SURF = pygame.display.set_mode((600, 600))  # Create a 600x600 window.
fps_clock = pygame.time.Clock()  # Frames-per-second timer.

# Don't change these:
START_X, START_Y = 50, 0
END_X, END_Y = 400, 0

# Get the cat image and set its position:
cats = []
for idx in range(6):  # There are six cats that will be animated:
    cat = {}
    cat['surface'] = pygame.Surface((80, 80))
    cat['surface'].fill((250, 0, 130))  # Use a pink 80x80 square for the "cat"
    # If you don't have a cat.png file, comment out this line:
    cat['surface'] = pygame.image.load('cat.png')
    cat['rect'] = cat['surface'].get_rect()  # Get the position & size rectangle of the cat.
    cat['rect'].left = START_X
    cat['rect'].top = START_Y + (idx * 100)
    cat['tween'] = TWEENS[idx]
    cats.append(cat)

i = 0.0  # The interpolation factor starts at 0.0.

font = pygame.font.Font('freesansbold.ttf', 28)

# Run the animation:
while True:
    # Terminate when the user closes the window, presses a key, or clicks the mouse:
    for event in pygame.event.get():  # Event handling loop.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            i = mouse_x / 600  # Set i based on mouse cursor position in the window.

    for idx in range(6):
        ti = cats[idx]['tween'](i)  # i is the input, ti is the tween output.

        # Set cat position based on the tweening interpolation factor.
        cats[idx]['rect'].left = START_X + (ti * (END_X - START_X))

    DISPLAY_SURF.fill(BG_COLOR)  # Clear the window.
    for idx in range(6):  # Draw all six cats.
        pygame.draw.rect(DISPLAY_SURF, (255, 255, 255), (START_X, START_Y + (idx * 100), cats[idx]['rect'].width, cats[idx]['rect'].height))  # Draw white rectangle at start.
        pygame.draw.rect(DISPLAY_SURF, (0, 0, 0), (END_X, END_Y + (idx * 100), cats[idx]['rect'].width, cats[idx]['rect'].height))  # Draw black rectangle at end.
        DISPLAY_SURF.blit(cats[idx]['surface'], cats[idx]['rect'])  # Draw the cat.

    # Set window caption to the current i value:
    pygame.display.set_caption('Move mouse to adjust: i = ' + str(round(i, 3)))

    pygame.display.update()  # Render the screen.
    fps_clock.tick(30)  # Pause enough to run at 30 frames per second.
