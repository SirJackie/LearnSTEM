from FrameBufferAxisSupport import Axis
import numpy

axis = Axis(768, 500, "Axis")
axis.Clear()
axis.Point(1, 1)
for i in numpy.arange(0, 3, 0.01):
    print(i)
    axis.Point(i, i)
axis.ViewBuffer()
