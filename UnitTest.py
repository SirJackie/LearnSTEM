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

    if not (equal(x11, 1.0) and equal(x12, -1.0) and
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
