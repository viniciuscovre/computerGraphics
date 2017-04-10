'''
EXERCISE
    Draw the straight line defined by the points (4,7) and (14,14) using the following algorithms for line generation:
        >>> Bresenham
        >>> DDA
'''

import bresenham
import pygame
pygame.init()

print("Choose one algorithm:\n\ta.Bresenham\n\tb.DDA")
answer = input()

if answer == 'a':
    resultingTuple = bresenham.getLine((4,7),(14,14))
# else:
#     resultingTuple = DDA((4,7),(14,14))

# Set 50x50 window
windowSurface = pygame.display.set_mode((50, 50), 0, 32)

# Set caption in the display
pygame.display.set_caption('Straight Line')

# pixArray gets the display of the pre-configured window
pixArray = pygame.PixelArray(windowSurface)

print(resultingTuple,"\n") # JUST FOR TESTING
# Printing in display
WHITE = (255,255,255)
for i in range(len(resultingTuple)):
    x = resultingTuple[i][0]
    y = resultingTuple[i][1]
    pixArray[x][y] = WHITE

# Update display with new values
pygame.display.update()