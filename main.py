import pygame
from constants import *


def main():
    pygame.init
    if pygame.get_init:
        print("Starting Asteroids!")
        print("Screen width: 1280")
        print("Screen height: 720")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
