# Simple pygame code!
import pygame
# from pygame.locals import*
import requests
from bs4 import BeautifulSoup
import threading
import psutil

# Settings
loginData = {
  'username': 'TC5550',
  'password': 'Krets5alfvik'
}
fetchStatsTime = 5
FPS = 10
# -----------

stats = {}

# s = requests.Session()
# loginPage = s.get("https://itch.io/login")
# soup = BeautifulSoup(loginPage.text, "html.parser")
# csrfToken = soup.select('meta[name="csrf_token"]')[0]["value"]

# loginData["csrf_token"] = csrfToken

# s.post("https://itch.io/login", data = loginData)

# def getStats():
#   print("Fetching stats...")

#   dashboard = s.get("https://itch.io/dashboard")
#   soup = BeautifulSoup(dashboard.text, "html.parser")
#   for div in soup.select(".stat_box"):
#     stats[div.select(".stat_label")[0].text.lower().strip()] = div.select(".stat_value")[0].text

# def set_interval(func, sec):
#   def func_wrapper():
#     global fetchInterval
#     fetchInterval = set_interval(func, sec)
#     func()
#   t = threading.Timer(sec, func_wrapper)
#   t.start()
#   return t

# fetchInterval = set_interval(getStats, fetchStatsTime)

pygame.init() # intialize the library
pygame.font.init()

fpsClock = pygame.time.Clock()

BACKGROUND = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

defaultFont = None
headerFont = pygame.font.SysFont(defaultFont, 120)
bodyFont = pygame.font.SysFont(defaultFont, 50)

# screen = pygame.display.set_mode((320 * 2, 240 * 2))
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

    y = 0
    for key, value in stats.items():
      drawText(bodyFont, key.title(), (10, 130 + y * 60), TEXTCOLOR)
      drawText(bodyFont, value, (250, 130 + y * 60), TEXTCOLOR)
      y += 1

    if y == 0:
      drawText(bodyFont, "Waiting for stats...", (10, 130), TEXTCOLOR)

    cpu = psutil.cpu_percent()
    drawText(bodyFont, "CPU: " + str(cpu) + "%", (10, 400), TEXTCOLOR)

    # drawText(bodyFont, 'Some Text ' + str(tick), (10, 130), TEXTCOLOR)

    # Flip the display
    pygame.display.flip()
    tick += 1
    fpsClock.tick(FPS)

# Quit the program
pygame.quit()
fetchInterval.cancel()