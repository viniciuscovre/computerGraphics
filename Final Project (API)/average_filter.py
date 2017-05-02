# Import a library of functions
import pygame, sys; from pygame.locals import *
import numpy as np
import constants; from constants import WIDTH, HEIGHT, MASK_SIZE, DIV

def Convole(wSurface, pixArray):
    for i in range(2, WIDTH + 1):
        for j in range(2, HEIGHT + 1):
            T = np.array([
                [wSurface.get_at((i-1,j-1)), wSurface.get_at((i-1,j)), wSurface.get_at((i-1,j+1))],
                [wSurface.get_at((i,j-1))  , wSurface.get_at((i,j))  , wSurface.get_at((i,j+1))  ],
                [wSurface.get_at((i+1,j-1)), wSurface.get_at((i+1,j)), wSurface.get_at((i+1,j+1))]
                ])
            # Removing 'A' part of RGBA gotten values
            # T = np.delete(T, [2], 2)

            # Reshaping tuple to a 9 rows and 3 collumns (RGB) tuple
            T = np.reshape(T,(DIV, MASK_SIZE + 1))

            # Getting sum of all values (for each R, G and B)
            T = [sum(x) for x in zip(*T)]

            # Divide each value by DIV. This is the new value of the central pixel.
            T = [x/DIV for x in T]

            # Print pixel with new color
            pixArray[i][j] = tuple(T)