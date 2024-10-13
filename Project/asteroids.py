import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            vector2 = pygame.math.Vector2.rotate(self.velocity, random_angle * -1) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS 
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 *1.2
            asteroid2.velocity = vector2 *1.2