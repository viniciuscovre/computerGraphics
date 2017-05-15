import dda
import bresenham_line
import bresenham_circle

def userInput():

    print("\n********************************")
    print("************ CG API ************")
    print("********************************")

    # Getting user's choice of algorithm
    print("\nChoose one algorithm:\n")
    print("\ta.DDA\n")
    print("\tb.Bresenham Line\n")
    print("\tc.Bresenham Circle\n")
    answer = str.lower(input())
    print("\n********************************")

    if answer == 'a':
        print("************** DDA *************")
        print("\nFrom point:\n")
        # +1 to place the pixel considering the padding
        x0 = int(input("\tx0: ")) + 1
        y0 = int(input("\ty0: ")) + 1
        print("\nTo point:\n")
        xF = int(input("\txF: ")) + 1
        yF = int(input("\tyF: ")) + 1
        listOfPoints = dda.getLine((x0,y0),(xF,yF))
    elif answer == 'b':
        print("******** BRESENHAM LINE ********")
        print("\nFrom point:\n")
        # +1 to place the pixel considering the padding
        x0 = int(input("\tx0: ")) + 1
        y0 = int(input("\ty0: ")) + 1
        print("\nTo point:\n")
        xF = int(input("\txF: ")) + 1
        yF = int(input("\tyF: ")) + 1
        listOfPoints = bresenham_line.getLine((x0,y0),(xF,yF))
    else:
        print("******* BRESENHAM CIRCLE *******")
        print("\nCenter:\n")
        xCenter = int(input("\txCenter: ")) + 1
        yCenter = int(input("\tyCenter: ")) + 1
        radius = int(input("\tRadius: "))
        listOfPoints = bresenham_circle.getCircle((xCenter,yCenter),radius)

    print("\n********************************\n")

    return listOfPoints