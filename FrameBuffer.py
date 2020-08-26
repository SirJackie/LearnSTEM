import pygame

class FrameBuffer:
    def __init__(self, width, height, caption="Frame Buffer"):

        self.width = width
        self.height = height
        self.caption = caption
        self.Screen = None

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
        # Create Screen
        self.Screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

        # Main Loop
        running = True
        while running:
            self.Screen.blit(self.FrameBuffer, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        # Clear the Variables
        self.Screen = None
        return
