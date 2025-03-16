import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (242, 243, 244), self.position, self.radius, 2)

    def get_velocity(self):
        return self.velocity

    def update(self, dt):
        velocity = self.get_velocity()
        self.position += velocity * dt