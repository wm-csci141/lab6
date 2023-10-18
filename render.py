import pygame
import sys
import math

# Global variables
width, height = 800, 800
win = None
x_offset, y_offset = 0, 0
scale = 1
mass_scale = 0.1
framerate = 60
clock = pygame.time.Clock()

def InitRender():
    global win
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('3-Body System')

def Render(system):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill((0, 0, 0))

    for body in system:
        mass, (x, y), _ = body
        pygame.draw.circle(
            win, 
            (255, 255, 255), 
            (int((x+x_offset) *scale), int((y+y_offset) *scale)), 
            int(mass**mass_scale))

    pygame.display.update()