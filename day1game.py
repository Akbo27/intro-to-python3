import pygame
import sys


class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self_color, (self.x, self.y), self.radius)

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

c = Circle(10, 100, 100)
c2 = Circle(5, 10, 100)
c3 = Circle(5, 10, 100)

vx = 4
vy = 5

vx2 = 3
vy2 = 3

window_width = 500
window_height = 500

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
bg_color = (30, 30, 30)
self_color = (0, 200, 0)  # green
pygame.display.set_caption("Flying circle")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(bg_color)
    c.draw(screen)
    c.move(vx,vy)
    c2.draw(screen)
    c2.move(vx2,vy2)

    c3.draw(screen)
    c3.move(vx2,vy2)

    if c.x > window_width or c.x < 0:
        vx = -vx

    if c.y > window_height or c.y < 0:
        vy = -vy

    if c2.x > window_width or c2.x < 0:
        vx2 = -vx2

    if c2.y > window_height or c2.y < 0:
        vy2 = -vy2

    pygame.display.flip()
    # Keep at 30 FPS or so
    clock.tick(30)

# Clean up
pygame.quit()
sys.exit()