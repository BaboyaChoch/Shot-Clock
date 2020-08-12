import pygame
from random import randrange


pygame.init()
win1 = pygame.display.set_mode((600, 400))
pygame.display.set_caption("BallTest")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
run = True
speed = 1
clock = pygame.time.Clock()


class Test:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw_circle(self, surface):
        pygame.draw(surface, self.color, (self.x, self.y), self.radius)

    def add_vel(self, vel):
        self.y += vel




# list of game balls
balls = [

    Test(green, randrange(600), 0, 20), Test(green, randrange(600), 0, 20),
    Test(green, randrange(600), 0, 20), Test(green, randrange(600), 0, 20),
    Test(green, randrange(600), 0, 20), Test(green, randrange(600), 0, 20)

]

while run:

    clock.tick(60)

    if not run:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    ball1 = Test(green, randrange(600), 0, 20)
    ball1.draw_circle(win1)

    # pygame.draw.circle(win1, green, (randrange(600),0), 20)

    pygame.display.update()

pygame.quit()
