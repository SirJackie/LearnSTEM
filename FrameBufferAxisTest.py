from FrameBufferAxisSupport import Axis
from multiprocessing import freeze_support
import numpy

freeze_support()
axis = Axis(768, 500, "Axis")
axis.Clear()
axis.Point(1, 1)
for i in numpy.arange(0, 3, 0.01):
    print(i)
    axis.Point(i, i)
if __name__ == "__main__":
    axis.ViewBuffer()
