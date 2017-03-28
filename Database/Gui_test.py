import pygame, sys
from pygame.locals import *

pygame.init()
screen_size = (700,900)
DISPLAYSURF = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Hello World')

#Main game loop
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
