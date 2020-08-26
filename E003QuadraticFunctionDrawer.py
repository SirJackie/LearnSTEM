from FrameBuffer import FrameBuffer

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


if __name__ == "__main__":
    fb = FrameBuffer(768, 500)
    fb.Fill((255, 255, 255))

    DrawAxis(fb, (0, 0, 0))

    fb.ViewBuffer()
