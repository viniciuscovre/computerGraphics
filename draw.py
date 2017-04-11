# Import a library of functions
import pygame, sys
from pygame.locals import *
import bresenham

# Initialize the game engine
pygame.init()

# Set (width X height) window
size = (500, 500)
windowSurface = pygame.display.set_mode(size, 0, 32)

# Set caption in the display
pygame.display.set_caption('Straight Line')

# pixArray gets the display of the pre-configured window
pixArray = pygame.PixelArray(windowSurface)

WHITE = (255, 255, 255)
resultingTuple = bresenham.getLine((4,7),(440,440))
for i in range(len(resultingTuple)):
    x = resultingTuple[i][0]
    y = resultingTuple[i][1]
    pixArray[x][y] = WHITE

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()