import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        
        pygame.draw.circle(screen, (242, 243, 244), self.position, SHOT_RADIUS, 2)

    def get_velocity(self):
        return self.velocity

    def update(self, dt):
        velocity = self.get_velocity()
        self.position += velocity * dt