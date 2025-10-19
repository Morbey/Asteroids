# this allows us to use code from the open-source pygame library throughout this file

import pygame

from pygame import Color
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill(Color("black"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.draw(screen)
        player.update(delta_time)
        pygame.display.flip()

        delta_time = clock.tick(60)/1000

if __name__ == "__main__":
    main()
