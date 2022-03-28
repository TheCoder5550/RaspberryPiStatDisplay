# Simple pygame code!
import pygame

pygame.init() # intialize the library

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:
    # Check if the user clicked the close button so that they dont keep playing for like
    # 2 years
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white (R, G, B) (also if you dont like lightmode, just replace it with (0,0,0))
    screen.fill((255, 255, 255))

    # Draw a blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Quit the program
pygame.quit()