# Simple pygame code!
import pygame

pygame.init() # intialize the library
pygame.font.init()

defaultFont = pygame.font.SysFont('Comic Sans MS', 50)
textSurface = defaultFont.render('Some Text', False, (0, 0, 0))

# Set up the drawing window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Run until the user asks to quit
running = True
while running:
    # Check if the user clicked the close button so that they dont keep playing for like
    # 2 years
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            running = False

    # Fill the background with white (R, G, B) (also if you dont like lightmode, just replace it with (0,0,0))
    screen.fill((255, 255, 255))

    # Draw a blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    screen.blit(textSurface, (0, 0))

    # Flip the display
    pygame.display.flip()

# Quit the program
pygame.quit()