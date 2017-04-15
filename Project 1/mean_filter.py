# Import a library of functions
import numpy as np
import constants
from constants import WIDTH, HEIGHT

filter = np.ones((3,3))
filter *= 1/9

for i in range(2, WIDTH + 1)
    for j in range(2, HEIGHT + 1)
