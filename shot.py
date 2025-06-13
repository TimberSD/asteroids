# pew pew ch3 l3
import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        
    def draw(self, screen):
#        print("Drawing shot at", self.position, "with radius", self.radius)
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt