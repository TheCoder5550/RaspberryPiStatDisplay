# Simple pygame code!
import pygame
from pygame.locals import*

pygame.init() # intialize the library
pygame.font.init()

BACKGROUND = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

defaultFont = None
headerFont = pygame.font.SysFont(defaultFont, 120)
bodyFont = pygame.font.SysFont(defaultFont, 50)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def drawText(font, text, pos, color):
  textSurface = font.render(text, False, color)
  screen.blit(textSurface, pos)

tick = 0
running = True

while running:
    # Check if the user clicked the close button so that they dont keep playing for like
    # 2 years
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE:
            running = False

    # Fill the background with white (R, G, B) (also if you dont like lightmode, just replace it with (0,0,0))
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(0, 0, 320 * 2, 240 * 2))

    # Draw a blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    drawText(headerFont, 'Dashboard', (10, 10), TEXTCOLOR)
    drawText(bodyFont, 'Some Text ' + str(tick), (10, 130), TEXTCOLOR)

    # Flip the display
    pygame.display.flip()
    tick += 1

# Quit the program
pygame.quit()