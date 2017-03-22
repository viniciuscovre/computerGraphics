''' 
EXERCISE
    Draw the straight line defined by the points (4,7) and (14,14) using the following algorithms for line generation:
        --> DDA
        --> Bresenham
'''

import pygame
pygame.init()

windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('XYZ')
pixArray = pygame.PixelArray(windowSurface)


WHITE = (255,255,255)
for i in range(10,300):
	pixArray[i][i] = WHITE

pygame.display.update()