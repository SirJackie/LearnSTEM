from FrameBufferAxisSupport import Axis
from math import sqrt
from tkinter import *
from numpy import arange


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

def DrawQuadraticFunction(ArgumentDict, axis):
    CriticalValue = 0.8

    if abs(ArgumentDict["a"]) <= CriticalValue:
        # Draw With X Axis
        for x in arange(-1 * axis.zoomedWidth / 2, axis.zoomedWidth / 2, 0.005):
            axis.Point(x, ArgumentDict["a"] * x * x + ArgumentDict["b"] * x + ArgumentDict["c"])

    elif abs(ArgumentDict["a"]) > CriticalValue:
        # Draw With Y Axis
        if ArgumentDict["a"] > 0:
            for y in arange(ArgumentDict["k"], axis.zoomedHeight / 2, 0.005):
                x1, x2 = usey2getx(y, ArgumentDict["a"], ArgumentDict["b"], ArgumentDict["c"])
                axis.Point(x1, y)
                axis.Point(x2, y)

        elif ArgumentDict["a"] < 0:
            for y in arange(ArgumentDict["k"], -1 * axis.zoomedHeight / 2, -0.005):
                x1, x2 = usey2getx(y, ArgumentDict["a"], ArgumentDict["b"], ArgumentDict["c"])
                axis.Point(x1, y)
                axis.Point(x2, y)


#
# Main Function
#

if __name__ == "__main__":

    ArgumentDict = {"a": 1.0,
                    "h": 0.0,
                    "k": 0.0,
                    "b": None,
                    "c": None
                    }

    axis = Axis(768, 500, caption="Quadratic Function Drawer")
    axis.Clear()

    ArgumentDict["a"], ArgumentDict["b"], ArgumentDict["c"] = VF2NF(
        ArgumentDict["a"],
        ArgumentDict["h"],
        ArgumentDict["k"]
    )

    DrawQuadraticFunction(ArgumentDict, axis)
    axis.ViewBuffer()

    #
    # Initialize FrameBufferAxisSupport
    #



    #
    # Tkinter Setup
    #

    window = Tk()





    def RefreshArguments(byWhatFormula):
        if byWhatFormula == "NF":
            ArgumentDict["a"], ArgumentDict["h"], ArgumentDict["k"] = NF2VF(
                ArgumentDict["a"],
                ArgumentDict["b"],
                ArgumentDict["c"]
            )
        elif byWhatFormula == "VF":
            ArgumentDict["a"], ArgumentDict["b"], ArgumentDict["c"] = VF2NF(
                ArgumentDict["a"],
                ArgumentDict["h"],
                ArgumentDict["k"]
            )

        axis.Clear()
        DrawQuadraticFunction(ArgumentDict, axis)
        axis.UpdateBuffer()

        # ScaleDict["ScaleNFA"].set(ArgumentDict["a"])
        # ScaleDict["ScaleNFB"].set(ArgumentDict["b"])
        # ScaleDict["ScaleNFC"].set(ArgumentDict["c"])
        # ScaleDict["ScaleVFA"].set(ArgumentDict["a"])
        # ScaleDict["ScaleVFH"].set(ArgumentDict["h"])
        # ScaleDict["ScaleVFK"].set(ArgumentDict["k"])


    def CallbackNFA(aString):
        ArgumentDict["a"] = float(aString)
        # RefreshArguments("NF")


    def CallbackNFB(bString):
        ArgumentDict["b"] = float(bString)
        # RefreshArguments("NF")


    def CallbackNFC(cString):
        ArgumentDict["c"] = float(cString)
        # RefreshArguments("NF")


    def CallbackVFA(aString):
        ArgumentDict["a"] = float(aString)
        RefreshArguments("VF")


    def CallbackVFH(hString):
        ArgumentDict["h"] = float(hString)
        RefreshArguments("VF")


    def CallbackVFK(kString):
        ArgumentDict["k"] = float(kString)
        RefreshArguments("VF")


    ScaleDict = {
        # "Label1": Label(window, text="一般式"),
        # "ScaleNFA": Scale(window,
        #                   label='a',  # Lable
        #                   from_=-3.0,  # Minimize Value
        #                   to=3.0,  # Maximize Value
        #                   resolution=0.01,  # Step
        #                   orient=HORIZONTAL,  # Direction
        #                   command=CallbackNFA,
        #                   ),
        # "ScaleNFB": Scale(window,
        #                   label='b',  # Lable
        #                   from_=-200000,  # Minimize Value
        #                   to=200000,  # Maximize Value
        #                   resolution=1,  # Step
        #                   orient=HORIZONTAL,  # Direction
        #                   command=CallbackNFB,
        #                   ),
        # "ScaleNFC": Scale(window,
        #                   label='c',  # Lable
        #                   from_=-100000000,  # Minimize Value
        #                   to=100000000,  # Maximize Value
        #                   resolution=1,  # Step
        #                   orient=HORIZONTAL,  # Direction
        #                   command=CallbackNFC,
        #                   ),
        # "LabelEmpty1": Label(window, text=""),
        # "LabelEmpty2": Label(window, text=""),
        "Label2": Label(window, text="顶点式"),
        "ScaleVFA": Scale(window,
                          label='a',  # Lable
                          from_=-3.0,  # Minimize Value
                          to=3.0,  # Maximize Value
                          resolution=0.01,  # Step
                          orient=HORIZONTAL,  # Direction
                          command=CallbackVFA,
                          ),
        "ScaleVFH": Scale(window,
                          label='h',  # Lable
                          from_=-1*(axis.zoomedWidth/2),  # Minimize Value
                          to=axis.zoomedWidth/2,  # Maximize Value
                          resolution=0.01,  # Step
                          orient=HORIZONTAL,  # Direction
                          command=CallbackVFH,
                          ),
        "ScaleVFK": Scale(window,
                          label='k',  # Lable
                          from_=-1*(axis.zoomedHeight/2),  # Minimize Value
                          to=axis.zoomedHeight/2,  # Maximize Value
                          resolution=0.01,  # Step
                          orient=HORIZONTAL,  # Direction
                          command=CallbackVFK,
                          ),
        "LabelEmpty3": Label(window, text="")
    }

    for i in ScaleDict.values():
        if isinstance(i, Scale):
            i.set(1)
        i.pack()

    window.mainloop()

    print("-------------")
    print(ArgumentDict)
    print("-------------")
