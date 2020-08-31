from FrameBuffer import FrameBuffer


class Axis(FrameBuffer):
    def __init__(self, width, height, caption="Frame Buffer", zoom=100):
        super().__init__(width, height, caption)
        self.zoom = zoom
        self.zoomedWidth = width / zoom
        self.zoomedHeight = height / zoom

    def Clear(self):
        super().Fill((255, 255, 255))

        # Draw X Axis
        for i in range(0, self.width):
            super().DrawPoint((i, int(self.height / 2 - 1)), (0, 0, 0))

        # Draw Y Axis
        for i in range(0, self.height):
            super().DrawPoint((int(self.width / 2 - 1), i), (0, 0, 0))

        # Draw X Arrow
        for i in range(0, 15):
            super().DrawPoint((int(self.width - 1) - i, int(self.height / 2 - 1) - i), (0, 0, 0))
            super().DrawPoint((int(self.width - 1) - i, int(self.height / 2 - 1) + i), (0, 0, 0))

        # Draw Y Arrow
        for i in range(0, 15):
            super().DrawPoint((int(self.width / 2 - 1) - i, 0 + i), (0, 0, 0))
            super().DrawPoint((int(self.width / 2 - 1) + i, 0 + i), (0, 0, 0))

    def Point(self, x, y):
        super().DrawPoint(
            (
                int(
                    (self.width / 2 - 1) + x*self.zoom
                ),
                int(
                    (self.height / 2 - 1) - y*self.zoom
                )
            ),
            (0, 0, 0))
