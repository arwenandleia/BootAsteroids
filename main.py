import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame_time = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()


    Player.containers = (updatable,drawable)
    Asteroid.containers = (all_asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (all_shots,updatable,drawable)


    dt = 0
    my_player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        updatable.update(dt)

        for asteroid in all_asteroids:
            if my_player.is_collision(asteroid):
                print('Game over!')
                sys.exit()

            for each_bullet in all_shots:
                if each_bullet.is_collision(asteroid):
                    asteroid.split()
                    each_bullet.kill()


        for thing in drawable:
            thing.draw(screen)


        pygame.display.flip()

        dt = pygame_time.tick(60)/1000
        


    

if __name__ == '__main__':
    main()