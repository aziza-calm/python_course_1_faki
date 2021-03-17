import random as rnd
import math
import pygame

from colors import *

FPS = 20
GRAVITY_ACCELERATION = 9.8  # Ускорение свободного падения для снаряда.
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


class Cannon:
    max_velocity = 10

    def __init__(self, x, y, width, height, ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shell_num = 10
        self.direction = math.pi / 4

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """
        pass  # TODO

    def fire(self, dt, shells, pos):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param pos: координаты мышки
        :param shells: список снарядов
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """
        x = self.x + self.width // 2
        y = self.y + self.height // 2
        v_x = pos[0] - self.x
        v_y = pos[1] - self.y
        shell = Shell(x, y, v_x, v_y)
        shells.append(shell)

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))


class Shell:
    standard_radius = 25

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = Shell.standard_radius
        self.color = COLORS[rnd.randint(0, len(COLORS) - 1)]
        self.is_alive = True

    def move(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """
        ax, ay = 0, GRAVITY_ACCELERATION
        self.x += self.Vx*dt + ax*(dt**2)/2
        self.y += self.Vy*dt + ay*(dt**2)/2
        self.Vx += ax*dt
        self.Vy += ay*dt
        if self.y + self.r >= SCREEN_HEIGHT:
            self.is_alive = False
        self.wall_direction_change()

    def wall_direction_change(self):
        """
        Меняет направление снаряда во время столкновений со стенками
        :return:
        """
        if self.x + self.r >= SCREEN_WIDTH:
            self.Vx = self.Vx * (-1)
        if self.x - self.r <= 0:
            self.Vx = self.Vx * (-1)
        if self.y - self.r <= 0:
            self.Vy = self.Vy * (-1)
        if self.y + self.r >= SCREEN_HEIGHT:
            self.Vy = self.Vy * (-1)

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (int(round(self.x)), int(round(self.y))), self.r)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """
        length = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return length <= self.r + other.r


class Target:
    standard_radius = 15

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = Target.standard_radius
        self.color = COLORS[rnd.randint(0, len(COLORS) - 1)]

    def move(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
            :return:
        """
        ax, ay = 0, GRAVITY_ACCELERATION
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += ay * dt
        # TODO: Шарики-мишени должны отражаться от стенок

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (int(round(self.x)), int(round(self.y))), self.r)

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """
        pass  #TODO


def generate_random_targets(number: int):
    targets = []
    for i in range(number):
        x = rnd.randint(0, SCREEN_HEIGHT)
        y = rnd.randint(0, SCREEN_HEIGHT)
        Vx = rnd.randint(-30, +30)
        Vy = rnd.randint(-30, +30)
        target = Target(x, y, Vx, Vy)
        targets.append(target)
    return targets


def game_main_loop():
    targets = generate_random_targets(10)
    shells = []
    clock = pygame.time.Clock()
    finished = False
    cannon = Cannon(0, SCREEN_HEIGHT * 0.9, SCREEN_WIDTH // 10, SCREEN_HEIGHT // 30)

    while not finished:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cannon.fire(dt, shells, event.pos)

        pygame.display.update()
        screen.fill(GRAY)

        for target in targets:
            target.move(dt)
        for target in targets:
            target.draw()
        for shell in shells:
            shell.move(dt)
            if shell.is_alive:
                shell.draw()
        cannon.draw()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.update()

    game_main_loop()
