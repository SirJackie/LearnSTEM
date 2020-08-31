import pygame
from multiprocessing import Process, Queue


def BufferViewer(width, height, caption, queue):
    # Create Screen
    Screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)

    # Main Loop
    running = True
    while running:
        try:
            SurfaceString = queue.get(False)
        except BaseException as e:
            # No Surface
            pass
        else:
            Screen.blit(pygame.image.fromstring(SurfaceString[0], SurfaceString[1], "RGB"), (0, 0))

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
        self.queue = None

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
        self.queue = Queue()
        p = Process(target=BufferViewer, args=(self.width, self.height, self.caption, self.queue))
        self.queue.put((pygame.image.tostring(self.FrameBuffer, "RGB"), self.FrameBuffer.get_size()))
        p.start()

    def UpdateBuffer(self):
        self.queue.put((pygame.image.tostring(self.FrameBuffer, "RGB"), self.FrameBuffer.get_size()))
