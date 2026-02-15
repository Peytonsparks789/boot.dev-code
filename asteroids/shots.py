from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt