import pygame
import os
from window.constants import *
from window.window import Window


FPS = 60
TYPE = TYPE_SELECTION
WINDOW_NAME = 'Selection Sort'
WINDOW_LOCATION = 100

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (WINDOW_LOCATION, WINDOW_LOCATION)
WIN = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_NAME)


def main():
    clock = pygame.time.Clock()
    window = Window(WIN, TYPE)
    
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                window.select(mouse_pos)

        window.update()

    pygame.quit()

main()