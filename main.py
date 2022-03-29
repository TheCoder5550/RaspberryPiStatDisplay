# Simple pygame code!
import pygame
# from pygame.locals import*
import requests
from bs4 import BeautifulSoup
import threading
# import psutil
import time
import yfinance as yf

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

# time.sleep(10) # wait for network

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
headerFont = pygame.font.SysFont(defaultFont, 80)
bodyFont = pygame.font.SysFont(defaultFont, 50)

screen = pygame.display.set_mode((320 * 2, 240 * 2))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.mouse.set_visible(False)

def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def drawText(font, text, pos, color):
  textSurface = font.render(text, False, color)
  screen.blit(textSurface, pos)

stock = "VOLV-B.ST"

oldFig = None
stockTimer = None
currentPrice = 0

def createStockChart():
  df = yf.download(tickers=stock, period='1d', interval='1m')

  global currentPrice
  currentPrice = df["Close"][-1]
  currentPrice = float("{0:.2f}".format(currentPrice))

  # matplotlib.rcParams.update({'text.color': "red",
  #                     'axes.labelcolor': "green"})

  fig = pylab.figure(figsize=[7, 3], # Inches
                    dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                    )

  global oldFig
  if oldFig:
    pylab.close(oldFig)

  oldFig = fig

  ax = fig.gca()

  remappedBackground = tuple(c / 255 for c in BACKGROUND)
  ax.set_facecolor(remappedBackground)
  fig.set_facecolor(remappedBackground)

  ax.spines['bottom'].set_color('white')
  # ax.spines['top'].set_color('white')
  ax.spines['left'].set_color('white')
  # ax.spines['right'].set_color('white')

  # ax.xaxis.label.set_color('red')
  ax.tick_params(axis='x', colors='white')
  ax.tick_params(axis='y', colors='white')

  ax.plot(df["Close"], linewidth=3)

  canvas = agg.FigureCanvasAgg(fig)
  canvas.draw()
  renderer = canvas.get_renderer()
  raw_data = renderer.tostring_rgb()
  size = canvas.get_width_height()

  global stockSurface
  stockSurface = pygame.image.fromstring(raw_data, size, "RGB")

  global stockTimer
  stockTimer = threading.Timer(5, createStockChart)
  stockTimer.start()

createStockChart()

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

        if event.type == pygame.MOUSEBUTTONUP:
          running = False

    # Fill the background with white (R, G, B) (also if you dont like lightmode, just replace it with (0,0,0))
    screen.fill(BACKGROUND)

    # Draw a blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    drawText(headerFont, 'Dashboard', (10, 10), TEXTCOLOR)

    # y = 0
    # for key, value in stats.items():
    #   drawText(bodyFont, key.title(), (10, 130 + y * 60), TEXTCOLOR)
    #   drawText(bodyFont, value, (250, 130 + y * 60), TEXTCOLOR)
    #   y += 1

    # if y == 0:
    #   drawText(bodyFont, "Waiting for stats...", (10, 130), TEXTCOLOR)

    # cpu = 0#psutil.cpu_percent()
    # drawText(bodyFont, "CPU: " + str(cpu) + "%", (10, 400), TEXTCOLOR)

    screen.blit(stockSurface, (-20, 130))

    drawText(bodyFont, stock, (10, 90), TEXTCOLOR)
    drawText(bodyFont, str(currentPrice) + " SEK", (250, 90), TEXTCOLOR)

    # drawText(bodyFont, 'Some Text ' + str(tick), (10, 130), TEXTCOLOR)

    # Flip the display
    pygame.display.flip()
    tick += 1
    fpsClock.tick(FPS)

# Quit the program
pygame.quit()
stockTimer.cancel()