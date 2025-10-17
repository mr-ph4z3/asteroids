import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import AsteroidField
from asteroid import *
from shot import Shot

def main():
    pygame.init
    if pygame.get_init:
        print("Starting Asteroids!")
        print("Screen width: 1280")
        print("Screen height: 720")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    

    while True:
        screen.fill("black")
        for p in drawable:
            p.draw(screen)
        updatable.update(dt)
        player.timer -= dt
        for a in asteroids:
            if player.collision(a):
                sys.exit("Game over!")
            for s in shots:
                if s.collision(a):
                    a.split()
                    s.kill()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (clock.tick(60) / 1000)


if __name__ == "__main__":
    main()
