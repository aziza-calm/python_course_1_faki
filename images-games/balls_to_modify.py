import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]

    def draw(self, screen):
        # Рисует сам шарик
        circle(screen, self.color, (self.x, self.y), self.r)

    def is_inside(self, pos):
        a = pos[0] - self.x
        b = pos[1] - self.y
        return a ** 2 + b ** 2 < self.r ** 2


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONUP:
            if ball.is_inside(event.pos):
                print("Inside!")
            else:
                print("Outside")
    ball = Ball()
    ball.draw(screen)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
