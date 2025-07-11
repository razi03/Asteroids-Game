import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()  # Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create screen

    while True:  # Game loop
        for event in pygame.event.get():  # Event loop
            if event.type == pygame.QUIT:
                return  # Exit the game

        screen.fill((0, 0, 0))  # Paint black
        pygame.display.flip()  # Refresh screen

if __name__ == "__main__":
    main()
