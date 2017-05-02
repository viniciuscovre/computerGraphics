''' ALGORITHM TO TRY TO IMPROVE AVERAGE_FILTER PERFORMANCE '''
# Import a library of functions
import pygame, sys; from pygame.locals import *
import numpy as np
import constants; from constants import WIDTH, HEIGHT, MASK_SIZE, DIV

def Convole(wSurface, pixArray):

    # Creating filter (+1 is for 'A' value in RGBA)
    filter = np.ones((MASK_SIZE, MASK_SIZE+1))
    filter = filter *

    # 3 dimensional filter: for R, G and B
    filter = np.array([filter,filter,filter])

    filter = x/DIV for x in filter

    for i in range(2, WIDTH + 1):
        for j in range(2, HEIGHT + 1):
            T = np.array([
                [wSurface.get_at((i-1,j-1)), wSurface.get_at((i-1,j)), wSurface.get_at((i-1,j+1))],
                [wSurface.get_at((i,j-1))  , wSurface.get_at((i,j))  , wSurface.get_at((i,j+1))  ],
                [wSurface.get_at((i+1,j-1)), wSurface.get_at((i+1,j)), wSurface.get_at((i+1,j+1))]
                ])

            # Reshaping tuple to a 9 rows and 3 collumns (RGB) tuple
            # T = np.reshape(T,(DIV, MASK_SIZE + 1))

            T = T*filter

            # Divide each value by DIV. This is the new value of the central pixel.
            T = [x/DIV for x in T]

            # Print pixel with new color
            pixArray[i][j] = tuple(T)