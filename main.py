import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
        player.draw(screen)
        player.update(dt)

        #update the display
        pygame.display.flip()

        #time
        dt = clock.tick(60)/1000    #time since last tick in seconds (limit game to 60fps)



    
if __name__ == "__main__":
    main()