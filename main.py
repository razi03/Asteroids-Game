import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()  # Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create screen

    clock = pygame.time.Clock()  # ✅ FIXED: Capital C
    dt = 0  # Delta time

    while True:  # Game loop
        for event in pygame.event.get():  # Event loop
            if event.type == pygame.QUIT:
                return  # Exit the game

        screen.fill((0, 0, 0))  # Paint black
        pygame.display.flip()  # Refresh screen

        dt = clock.tick(60) / 1000  # Frame limiter & delta time

if __name__ == "__main__":
    main()
