import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *
import sys




def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(x =SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        player.timer -= dt
        updatable.update(dt)


        for object in drawable:
            object.draw(screen)

        for object in asteroids:
            if object.detect_collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if shot.detect_collision(object):
                    object.split()


        pygame.display.flip()
        dt = clock.tick(60) / 1000


    

    










if __name__ == "__main__":
    main()