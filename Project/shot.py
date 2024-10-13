import pygame
from constants import *
from circleshape import CircleShape 

class Shots(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, SHOT_RADIUS) 
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt  
