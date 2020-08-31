import pygame
from multiprocessing import Process


class SurfaceCompatible(pygame.Surface):
    _pixels_address = None

    def GetOriginalSurface(self):
        pygame.Surface((super().get_width(), super().get_height()), 0, self)


def PickleSurface(yourSurface):
    return {
        "Width": yourSurface.get_width(),
        "Height": yourSurface.get_height(),
        "Address": yourSurface._pixels_address
    }


def UnpickleSurface(pickledSurface):
    tmpSurface = SurfaceCompatible((pickledSurface["Width"], pickledSurface["Height"]))
    tmpSurface._pixels_address = pickledSurface["Address"]
    return tmpSurface


def BufferViewer(width, height, caption, pickledSurface):
    # Create Screen
    Screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)

    Surface = UnpickleSurface(pickledSurface)

    # Main Loop
    running = True
    while running:
        Screen.blit(Surface, (0, 0))
        print(Surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    # Clear the Variables
    Screen = None
    return


class FrameBuffer:
    def __init__(self, width, height, caption="Frame Buffer"):
        self.width = width
        self.height = height
        self.caption = caption

        # Create Frame Buffer
        self.FrameBuffer = pygame.Surface((width, height))

    def Fill(self, color):
        self.FrameBuffer.fill((color[0], color[1], color[2], 255))

    def GetColor(self, position):
        originColor = self.FrameBuffer.get_at(position)
        return originColor[0], originColor[1], originColor[2]

    def DrawPoint(self, position, color):
        self.FrameBuffer.set_at(position, (color[0], color[1], color[2], 255))

    def ViewBuffer(self):
        p = Process(target=BufferViewer, args=(self.width, self.height, self.caption, PickleSurface(self.FrameBuffer)))
        p.start()

if __name__ == "__main__":
    a = pygame.Surface((768, 500))
    a.set_at((100, 100), (123, 134, 145))
    a.unlock()

    pickledA = PickleSurface(a)

    b = UnpickleSurface(pickledA)
    print(b.get_at((100, 100)))
