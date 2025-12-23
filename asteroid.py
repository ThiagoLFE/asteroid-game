from circleshape import CircleShape
import pygame
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split") 
        angle_news_asteroids = uniform(20, 50)
        
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)

        asteroid1.velocity = (self.velocity * 1.2).rotate(angle_news_asteroids)
        asteroid2.velocity = (self.velocity * 1.2).rotate(angle_news_asteroids * -1)

    