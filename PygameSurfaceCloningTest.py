import pygame

Surface = pygame.Surface

class SurfaceCompatible(pygame.Surface):
    _pixels_address = None

a = Surface((100, 100))
b = SurfaceCompatible((1, 1))


b._pixels_address = a._pixels_address

c = Surface((100, 100), 0, b)

print(c.get_width())
