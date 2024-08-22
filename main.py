import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from shoot import *

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Creating window measure
    pygame.display.set_caption("Andrés Asteroid Game") # Name of the window
    running = True
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Shoot.containers = (shots, updatable, drawable)
    
    player = Player(x,y) # Player object
    asteroid_field = AsteroidField()


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for updating in updatable:
            updating.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                running = False
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)
        
        asteroid_field.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()