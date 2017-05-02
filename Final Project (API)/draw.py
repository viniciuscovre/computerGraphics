'''
Computer Graphics - Denis Salvadeo - Final Project (API)
Unesp - Rio Claro
Group: Vinicius Covre, Bianca Privati, Felipe Pipoca
'''

# Import a library of functions
import pygame, sys; from pygame.locals import *
import constants; from constants import SIZE, WHITE
import menu
import average_filter

# Interact with user
listOfPoints = menu.userInput()

# Initialize the game engine
pygame.init()

# Set (width X height) window
wSurface = pygame.display.set_mode(SIZE, 0, 32)

# Set caption in the display
pygame.display.set_caption('CG API')

# pixArray gets the display of the pre-configured window
pixArray = pygame.PixelArray(wSurface)

# Print obtained pixels
for i in range(len(listOfPoints)):
    x = listOfPoints[i][0]
    y = listOfPoints[i][1]
    pixArray[x][y] = WHITE

# draw the window onto the screen
pygame.display.update()

# Apply average filter
print("Applying Average Filter...")
input("[press any key to continue]")
average_filter.Convole(wSurface, pixArray)

# Draw the window onto the screen
pygame.display.update()

# # Exit pygame and end program execution
# input("\n[press any key to quit]")
# pygame.quit()
# sys.exit()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()