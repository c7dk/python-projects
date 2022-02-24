"""
# 1. simplest setup

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False


    pygame.display.update()

pygame.quit()
"""
# --------------------
# 2. drawing a circle

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

green = (0, 255, 0)
radius = 50

keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    pygame.draw.circle(screen, green, (100, 100), radius)

    pygame.display.update()

pygame.quit()
