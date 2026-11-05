


try:
    import pygame
except ModuleNotFoundError:
    pygame = None


class _Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.speed = 5
        rect_type = pygame.Rect if pygame is not None else _Rect
        self.rect = rect_type(self.x, self.y, self.width, self.height)

    def draw(self, surface_):
        if pygame is None:
            raise RuntimeError("pygame is required to draw the player")
        pygame.draw.rect(surface_, (0, 255, 0), self.rect)

    def move_left(self):
        self.x -= self.speed
        self.rect.x = self.x

    def move_right(self):
        self.x += self.speed
        self.rect.x = self.x