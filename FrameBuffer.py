import pygame
from multiprocessing import Process
from multiprocessing import freeze_support
# freeze_support()

def BufferViewer(width, height, caption, FrameBufferAddress):
    # Create Screen
    Screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    surfaceTmp = pygame.Surface((1, 1))
    print(surfaceTmp.__getattribute__)
    surfaceTmp._pixels_address = FrameBufferAddress


    # Main Loop
    running = True
    while running:
        Screen.blit(surfaceTmp, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    # Clear the Variables
    self.Screen = None
    return

class FrameBuffer:
    def __init__(self, width, height, caption="Frame Buffer"):

        self.width = width
        self.height = height
        self.caption = caption

        # Create Frame Buffer
        surfaceTmp = pygame.Surface((width, height))
        self.FrameBuffer = surfaceTmp
        self.FrameBufferAddress = surfaceTmp._pixels_address

    def Fill(self, color):
        self.FrameBuffer.fill((color[0], color[1], color[2], 255))

    def GetColor(self, position):
        originColor = self.FrameBuffer.get_at(position)
        return originColor[0], originColor[1], originColor[2]

    def DrawPoint(self, position, color):
        self.FrameBuffer.set_at(position, (color[0], color[1], color[2], 255))

    def ViewBuffer(self):
        p = Process(target=BufferViewer, args=(self.width, self.height, self.caption, self.FrameBufferAddress))
        freeze_support()
        p.start()

