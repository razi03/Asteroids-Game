import pygame
from constants import *
from player import Player  # ✅ Don’t forget this!

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # ✅ Instantiate player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)         # Update input/movement
        screen.fill((0, 0, 0))    # Clear screen
        player.draw(screen)       # Draw player
        pygame.display.flip()     # Show updated frame

        dt = clock.tick(60) / 1000  # Frame timing (delta time)
