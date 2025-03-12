import pygame
import sys
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from Shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers= (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    
    

    #clock settings
    clock = pygame.time.Clock()
    dt= 0



    #game loop
    while True:
        #check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Fill the screen with black 
        screen.fill("black")
        updatable.update(dt)

        #check for collisions
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()



        for drawable_object in drawable:
            drawable_object.draw(screen)

        #update the display
        pygame.display.flip()

        #time
        dt = clock.tick(60)/1000    #time since last tick in seconds (limit game to 60fps)



    
if __name__ == "__main__":
    main()