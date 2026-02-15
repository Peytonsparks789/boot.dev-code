import pygame
import random

from logger import log_event
from constants import ASTEROID_MIN_RADIUS
from constants import LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # Foreach new asteroid
        asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, asteroid1_radius)
        asteroid1.velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2

        asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid2 = Asteroid(self.position.x, self.position.y, asteroid2_radius)
        asteroid2.velocity = self.velocity.rotate(random.uniform(-20, -50)) * 1.2