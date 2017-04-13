points = []

def getCircle(center, radius):
    """
    Bresenham's Circle Algorithm
    Produces a list of tuples/pixels (x,y) to be printed
    """
    # Setup initial conditions
    x = 0
    y = radius
    d = 1 - radius
    xCenter, yCenter = center

    # Get initial points
    getPoints(xCenter, yCenter, x, y)

    # Iterate to generate points in the first octant
    while x < y:

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

        # Get subsequent points
        getPoints(xCenter, yCenter, x, y)

    return points

def getPoints(xCenter, yCenter, x, y):

    coord = (xCenter + x, yCenter + y)
    points.append(coord)

    coord = (xCenter + y, yCenter + x)
    points.append(coord)

    coord = (xCenter + y, yCenter - x)
    points.append(coord)

    coord = (xCenter + x, yCenter - y)
    points.append(coord)

    coord = (xCenter - x, yCenter - y)
    points.append(coord)

    coord = (xCenter - y, yCenter - x)
    points.append(coord)

    coord = (xCenter - y, yCenter + x)
    points.append(coord)

    coord = (xCenter - x, yCenter + y)
    points.append(coord)