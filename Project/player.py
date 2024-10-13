from circleshape import CircleShape
from constants import * 
import pygame 
from shot import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0 
        self.shot_timer = 0 
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255) , self.triangle(), width= 2) 


    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED* dt)
    
    def move(self, dt):
        foward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += foward * PLAYER_SPEED * dt
    
    def shoot(self, dt):
        player_shot = Shots(self.position.x,self.position.y, SHOT_RADIUS)
        player_shot.velocity = pygame.Vector2(0,1)        
        player_shot.velocity = pygame.math.Vector2.rotate(player_shot.velocity, self.rotation)
        player_shot.velocity *= PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot(dt)
        

        self.shot_timer -= dt
