# Asteroid Class file
import pygame
import random
from constants import *
from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
# Asteroid Split CH3 L6
    def split(self):
        self.kill()
        split_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            a = self.velocity.rotate((-split_angle))
            b = self.velocity.rotate((split_angle))
            asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid.velocity = a * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid.velocity = b * 1.2