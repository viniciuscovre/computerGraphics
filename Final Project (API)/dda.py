def getLine(start, end):
    """
    DDA Algorithm
    Produces a list of tuples/pixels (x,y) to be printed
    """
    # Setting up initial values
    points = []
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Calculating the number of interations
    iter = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Increment has to be 1 or -1 in the right axis
    x_inc = dx/iter
    y_inc = dy/iter

    # Getting initial point
    x = x1
    y = y1

    # Iterating to generate points of the line
    points.append((x,y))
    for i in range(0, iter):
        x += x_inc
        y += y_inc
        points.append((round(x),round(y)))

    return points