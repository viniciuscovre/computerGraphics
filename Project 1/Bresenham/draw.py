'''
Computer Graphics - Denis Salvadeo - Project 1 (part 1)
Unesp - Rio Claro
Group: Vinicius Covre, Bianca Privati, Felipe Pipoca
'''

# Import a library of functions
import pygame, sys
from pygame.locals import *
import bresenham

# Getting user's choice of algorithm
print("Choose one algorithm:\n")
print("\ta.Bresenham Line\n")
print("\tb.Bresenham Circle\n\t")
answer = input()
print("\n********************************")

if str.lower(answer) == 'a':
    pygame.display.set_caption('Bresenham Line')
    print("******** BRESENHAM LINE ********")
    print("\nFrom point:\n")
    x0 = int(input("\tx0:"))
    y0 = int(input("\ty0:"))
    print("\nTo point:\n")
    xF = int(input("\txF:"))
    yF = int(input("\tyF:"))
    resultingTuple = bresenham.getLine((x0,y0),(xF,yF))
else:
    pygame.display.set_caption('Bresenham Circle')
    print("******* BRESENHAM CIRCLE *******")

# Initialize the game engine
pygame.init()

# Set (width X height) window
size = (500, 500)
windowSurface = pygame.display.set_mode(size, 0, 32)

# Set caption in the display
pygame.display.set_caption('Straight Line')

# pixArray gets the display of the pre-configured window
pixArray = pygame.PixelArray(windowSurface)

# Print obtained pixels
WHITE = (255, 255, 255)
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