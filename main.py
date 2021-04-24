import math
import pygame
import numpy as np
from constants import Width, Height
import random
from Vector import *
from Shapes import *
import colorsys

size = (Width, Height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cloth Simulation")
clock = pygame.time.Clock()

particles = []
for i in range(4):
    for j in range(20):
        x = random.randint(20, Width-20)
        y = random.randint(20, Height-20)
        old = random.randint(1, 200)
        size = random.randint(8, 20)
        particles.append(Point(Vector2(x, y), Vector2(x-old, y-old), size))

b = Box(Vector2(10, 10), 10, 10, 4)
c = Rope(Vector2(10, 10), 20, 15, 8, 7)
d = Cloth(Vector2(Width//2, 200), 10, 10)
toggle = True
run = True
while run:
    clock.tick(30)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;

    if pygame.mouse.get_pressed()[0]:
        mousePosition = pygame.mouse.get_pos()
        if toggle == True:
            d.vertices[0].position = Vector2(mousePosition[0], mousePosition[1])
        else:
            d.vertices[-1].position = Vector2(mousePosition[0], mousePosition[1])
        # c.vertices[0].update()

    if pygame.mouse.get_pressed()[2]:
        toggle = not toggle

    # for p in particles:
    #     p.update()
    #     p.Constraint()
    #     p.Draw(screen)
    d.Update()
    d.Draw(screen, True)
    d.ConstraintPolygon()
    pygame.display.flip()
pygame.quit()
