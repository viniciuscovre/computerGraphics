def getLine(start, end):
    """
    Bresenham's Line Algorithm
    Produces a list of tuples/pixels (x,y) to be printed
    """
    # Setting up initial values
    points = []
    x1, y1 = start
    x2, y2 = end
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Checking if line is close to y-axis
    invertedCoordinates = False
    if dy > dx:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        invertedCoordinates = True

    # Get the initial point as the closest to the center (0,0)
    invertedPoints = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        invertedPoints = True

    # Recalculating differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculating d value
    d = int(dx / 2.0)

    # Calculating increment in y
    yInc = 1 if y1 < y2 else -1

    # Iterating to generate points of the line
    y = y1
    for x in range(x1, x2 + 1):
        pixel = (y, x) if invertedCoordinates else (x,y)
        points.append(pixel)
        d -= abs(dy)
        if d < 0:
            y += yInc
            d += dx

    # If the start and end points are inverted, reverse the list
    if invertedPoints:
        points.reverse()
    return points