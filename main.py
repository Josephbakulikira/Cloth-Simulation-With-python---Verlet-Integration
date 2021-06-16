import math
import pygame
import numpy as np
from constants import Width, Height
import random
from Vector import *
from Shapes import *
from ui import *
from uiParameters import *
import colorsys

size = (Width, Height)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cloth Simulation")
clock = pygame.time.Clock()


textI = "0"
keyPressed = False
d = Cloth(Vector2(Width//2 - 200, Height//2 - 120), rowsInput.value, colsInput.value, spacingInput.value)
toggle = False

SpaceButtonPressed = False
clicked = False
showUI = False
run = True
backSpace = False

while run:
    deltaTime = clock.tick(30)

    if runButton.state == True:
        d = Cloth(Vector2(Width//2 - 200, Height//2 - 120), rowsInput.value, colsInput.value,
                        spacingInput.value, radiusInput.value, thicknessInput.value, toggleVertical.state,
                        toggleHorizontal.state, toggleDiagonal1.state, toggleDiagonal2.state)
        runButton.state = False

    screen.fill((3, 4, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                SpaceButtonPressed = True
            if event.key == pygame.K_u:
                showUI = True

            textI = pygame.key.name(event.key)
            keyPressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                backSpace = True

    if pygame.mouse.get_pressed()[2]:
        for vertice in d.vertices:
            vertice.isClicked=False

    d.Update(toggle, SpaceButtonPressed)
    d.showPoint = showPoint.state
    d.radiusPoint = radiusInput.value
    d.Draw(screen)
    d.ConstraintPolygon()

    #render ui
    if showUI:
        panel.Render(screen)
        runButton.Render(screen)
        connections.Render(screen)
        verticalText.Render(screen)
        horizontalText.Render(screen)
        diagonal1Text.Render(screen)
        diagonal2Text.Render(screen)
        showpointText.Render(screen)
        rowsText.Render(screen)
        colsText.Render(screen)
        radiusText.Render(screen)
        thicknessText.Render(screen)
        spacingText.Render(screen)
        toggleVertical.Render(screen,clicked)
        toggleHorizontal.Render(screen,clicked)
        toggleDiagonal1.Render(screen,clicked)
        toggleDiagonal2.Render(screen,clicked)
        showPoint.Render(screen, clicked)
        rowsText.Render(screen)
        colsText.Render(screen)
        rowsInput.Render(screen, textI, backSpace, keyPressed)
        colsInput.Render(screen, textI, backSpace, keyPressed)
        radiusInput.Render(screen, textI, backSpace, keyPressed)
        thicknessInput.Render(screen, textI, backSpace, keyPressed)
        spacingInput.Render(screen, textI, backSpace, keyPressed)
    else:
        showuiText.Render(screen)
    backSpace = False
    keyPressed = False
    pygame.display.flip()
    clicked = False
    SpaceButtonPressed = False
pygame.quit()
