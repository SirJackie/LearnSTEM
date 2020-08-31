from FrameBufferAxisSupport import Axis
from math import sqrt


#
# Quadratic Supporting Functions
#

# Convert Normal Formula to Vertex Formula
def NF2VF(a, b, c):
    return a, -1 * b / 2 * a, (4 * a * c - b * b) / 4 * a

# Convert Vertex Formula to Normal Formula
def VF2NF(a, h, k):
    # return a, b, c
    return a, -2 * a * h, a * h * h + k

# Use Y to Get X in Quadratic Function
def usey2getx(y, a, b, c):
    try:
        return (-1 * b + sqrt(b * b - 4 * a * c + 4 * a * y)) / (2 * a), \
               (-1 * b - sqrt(b * b - 4 * a * c + 4 * a * y)) / (2 * a)  # (2 * a) must have bracket
    except ValueError as e:
        raise ValueError("This Quadratic Functions DOES NOT across y = %s" % y)
        return None, None


#
# Unit Test
#

# Test If Float Is Equal
def equal(a, b):
    return abs(float(a) - float(b)) < 0.0005

# Unit Test Function
def UnitTest():
    result = ""


    #
    # Test1: VF2NF() and NF2VF()
    #

    a, b, c = 1, 2, 3
    print(a, b, c)
    a, h, k = NF2VF(a, b, c)
    print(a, h, k)
    a2, b2, c2 = VF2NF(a, h, k)
    print(a2, b2, c2)
    if not (equal(a, a2) and equal(b, b2) and equal(c, c2)):
        result += "Test1 Rejected\n"


    #
    # Test2 : usey2getx()
    #

    a, b, c = VF2NF(1, 0, 0)
    x11, x12 = usey2getx(1, a, b, c)
    x21, x22 = usey2getx(4, a, b, c)
    x31, x32 = usey2getx(9, a, b, c)
    x41, x42 = usey2getx(16, a, b, c)
    x51, x52 = usey2getx(25, a, b, c)

    hasMathAreaError = False
    try:
        usey2getx(-5, a, b, c)
    except ValueError as e:
        hasMathAreaError = True

    if not(equal(x11, 1.0) and equal(x12, -1.0) and
           equal(x21, 2.0) and equal(x22, -2.0) and
           equal(x31, 3.0) and equal(x32, -3.0) and
           equal(x41, 4.0) and equal(x42, -4.0) and
           equal(x51, 5.0) and equal(x52, -5.0) and
           hasMathAreaError is True):
        result += "Test2 Rejected\n"


    #
    # Output the Result
    #

    if result == "":
        print("Accepted")
    else:
        print(result)


#
# Main Function
#

if __name__ == "__main__":


    #
    # Initialize FrameBufferAxisSupport
    #

    axis = Axis(768, 500, caption="Quadratic Function Drawer")
    axis.Clear()


    #
    # Get And Calculate a, b, c, h, k
    #

    a, b, c, h, k = None, None, None, None, None

    # mode = input("Please Select Drawing Mode:\n"
    #              "1.Vertex Formula (a, h, k)\n"
    #              "2.Normal Formula (a, b, c)\n")
    mode = "1"

    if mode == "1":
        # a, h, k = map(float, input("Please Input a, h, k\n"
        #                            "(Use Space to Split)\n").split(" "))
        a, h, k = -0.1, 0, 0

        afunc = lambda a: str(a)
        hfunc = lambda h: "- " + str(h) if h > 0 else "+ " + str(-1 * h)
        kfunc = lambda k: "+ " + str(k) if k > 0 else "- " + str(-1 * k)

        print("Got Cha! y =", afunc(a), "( x", hfunc(h), ")²", kfunc(k))

        a, b, c = VF2NF(a, h, k)

    elif mode == "2":
        a, b, c = map(float, input("Please input a, b, c\n"
                                   "(Use Space to Split)\n").split(" "))

        ax2 = lambda a: str(a) + "x²"
        bx = lambda b: "+ " + str(b) + "x" if b > 0 else "- " + str(-1 * b) + "x"
        cfunc = lambda c : "+ " + str(c) if c > 0 else "- " + str(-1 * c)

        print("Got Cha! y =", ax2(a), bx(b), cfunc(c))

        a, h, k = NF2VF(a, b, c)

    print(a, b, c)


    #
    # Start Drawing
    #

    CriticalValue = 0.05

    if abs(a) <= CriticalValue:
        # Draw With X Axis
        for x in range(int(-1 * axis.width / 2), int(axis.width / 2)):
            axis.Point(x, a * x * x + b * x + c)

    elif abs(a) > CriticalValue:
        # Draw With Y Axis
        if a > 0:
            for y in range(int(k), int(axis.height / 2)):
                x1, x2 = usey2getx(y, a, b, c)
                axis.Point(x1, y)
                axis.Point(x2, y)

        elif a < 0:
            for y in range(int(k), int(-1 * axis.height/2), -1):
                x1, x2 = usey2getx(y, a, b, c)
                axis.Point(x1, y)
                axis.Point(x2, y)


    #
    # Show the Result
    #

    axis.ViewBuffer()


