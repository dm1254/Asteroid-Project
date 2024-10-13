import pygame 
from constants import *
from player import Player
from asteroidfield import AsteroidField 
from asteroids import Asteroid  
from shot import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers =(updatables,)
    Shots.containers = (updatables, drawables, shot)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatables:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.collision(player) is True:
                raise SystemExit ("Game Over!")
        
        for obj in asteroids:        
            for bullet in shot:
                if obj.collision(bullet) is True:
                    obj.split()
                    bullet.kill()
                    
                    
        screen.fill("black")
        
        for obj in drawables:
            obj.draw(screen)

                    
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
