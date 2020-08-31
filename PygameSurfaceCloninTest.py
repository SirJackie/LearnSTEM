import pygame

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

if __name__ == "__main__":
    a = pygame.Surface((768, 500))
    a.set_at((100, 100), (123, 134, 145))
    a.unlock()

    pickledA = PickleSurface(a)

    b = UnpickleSurface(pickledA)
    print(b.get_at((100, 100)))