import pygame
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import *

class Player(CircleShape):
    player_timer = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
# Player Sprite draw    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
# Player movement rotation    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
# Player Move method
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
# Player shoot method
    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity *= PLAYER_SHOOT_SPEED
#        print("shots fired at", self.position.x, self.position.y)
        
# Player update method
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
# Forward and reverse keys
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.player_timer > 0:
                return False
            else:
                self.player_timer += PLAYER_SHOOT_COOLDOWN
                self.shoot()
        else:
            self.player_timer -= dt