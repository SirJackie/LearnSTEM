from FrameBuffer import FrameBuffer


#
# Axis Supporting Functions
#

def DrawAxis(fb, color):
    width = fb.width
    height = fb.height

    # Draw X Axis
    for i in range(0, width):
        fb.DrawPoint((i, int(height/2-1)), color)

    # Draw Y Axis
    for i in range(0, height):
        fb.DrawPoint((int(width/2-1), i), color)

    # Draw X Arrow
    for i in range(0, 15):
        fb.DrawPoint((int(width-1) - i, int(height/2-1) - i), color)
        fb.DrawPoint((int(width-1) - i, int(height/2-1) + i), color)

    # Draw Y Arrow
    for i in range(0, 15):
        fb.DrawPoint((int(width/2-1) - i, 0 + i), color)
        fb.DrawPoint((int(width/2-1) + i, 0 + i), color)

# Convert Point in Axis Into Point in Screen
def p(x, y, fb):
    return int((fb.width / 2 - 1) + x), int((fb.height / 2 - 1) - y)


#
# Converting Functions
#

# Convert Normal Formula to Vertex Formula
def NF2VF(a, b, c):
    return a, -1 * b / 2 * a, (4 * a * c - b * b) / 4 * a

# Convert Vertex Formula to Normal Formula
def VF2NF(a, h, k):
    # return a, b, c
    return a, -2 * a * h, a * h * h + k


#
# Unit Test
#

def equal(a, b):
    return abs(float(a) - float(b)) < 0.0005

def UnitTest():
    result = ""

    # Test1: VF2NF
    a, b, c = 1, 2, 3
    print(a, b, c)
    a, h, k = NF2VF(a, b, c)
    print(a, h, k)
    a2, b2, c2 = VF2NF(a, h, k)
    print(a2, b2, c2)
    if not (equal(a, a2) and equal(b, b2) and equal(c, c2)):
        result += "Test1 Rejected\n"

    # Output the Result
    if result == "":
        print("Accepted")
    else:
        print(result)


#
# Main Function
#

if __name__ == "__main__":
    fb = FrameBuffer(768, 500, caption="Quadratic Function Drawer")
    fb.Fill((255, 255, 255))

    DrawAxis(fb, (0, 0, 0))

    fb.DrawPoint(p(10, 10, fb), (0, 0, 0))

    # mode = input("Please Select Drawing Mode:\n"
    #              "1.Vertex Formula (a, h, k)\n"
    #              "2.Normal Formula (a, b, c)\n")
    #
    # if mode == "1":
    #     a, h, k = map(float, input("Please Input a, h, k\n"
    #                                "(Use Space to Split)\n").split(" "))
    #
    #     afunc = lambda a: str(a)
    #     hfunc = lambda h: "- " + str(h) if h > 0 else "+ " + str(-1 * h)
    #     kfunc = lambda k: "+ " + str(k) if k > 0 else "- " + str(-1 * k)
    #
    #     print("Got Cha! y =", afunc(a), "( x", hfunc(h), ")²", kfunc(k))
    #
    # elif mode == "2":
    #     a, b, c = map(float, input("Please input a, b, c\n"
    #                                "(Use Space to Split)\n").split(" "))
    #
    #     ax2 = lambda a: str(a) + "x²"
    #     bx = lambda b: "+ " + str(b) + "x" if b > 0 else "- " + str(-1 * b) + "x"
    #     cfunc = lambda c : "+ " + str(c) if c > 0 else "- " + str(-1 * c)
    #
    #     print("Got Cha! y =", ax2(a), bx(b), cfunc(c))
    #
    fb.ViewBuffer()


