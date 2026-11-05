import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface_):
        pygame.draw.rect(surface_, (0, 255, 0), self.rect)

    def move_left(self):
        self.x -= self.speed
        self.rect.x = self.x

    def move_right(self):
        self.x += self.speed
        self.rect.x = self.x