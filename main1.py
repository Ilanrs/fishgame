def main ()
    print("Hello world")


if __name__ == "__main__"
    main()


import sys, pygame
from pygame.locals import*

pygame.init()
screen_info = pygame.display.Info()


size = (width, height)v = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0,127,255)