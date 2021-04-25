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


d = Cloth(Vector2(Width//2 - 200, Height//2 - 120), 20, 10, 20)

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
            d.vertices[19].position = Vector2(mousePosition[0], mousePosition[1])

    if pygame.mouse.get_pressed()[2]:
        toggle = not toggle

    d.Update()
    d.Draw(screen, True)
    d.ConstraintPolygon()
    pygame.display.flip()
pygame.quit()
