import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for x in range(-300,300):
        y = f(x / 50)
        screen_x = int(w / 2 + x)
        screen_y = int(h/2 - y * 50)
        x = random.randint(0, w)
        y = random.randint(0, h)
        if 0 <= screen_x < w and 0 <= screen_y < h:
            screen.set_at((screen_x, screen_y), (255, 255, 255))
        screen.set_at((x, y), (255, 255, 255))

    pygame.display.flip()

pygame.quit()