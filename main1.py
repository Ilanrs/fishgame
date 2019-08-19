import sys, pygame
from pygame.locals import*


def main():
    print("Hello world")


if __name__ == "__main__":
    main()

pygame.init()
screen_info = pygame.display.Info()


size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)