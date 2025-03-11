import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    while True:
        #check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Fill the screen with black 
        screen.fill("black")

        #update the display
        pygame.display.flip()


    
if __name__ == "__main__":
    main()