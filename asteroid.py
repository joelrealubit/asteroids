import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"WHITE", self.position ,self.radius,LINE_WIDTH)
    
    def update(self, dt):
       self.position+=self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rnum = random.uniform(20,50)
        new_movement_1 = self.velocity.rotate(rnum)
        new_movement_2 = self.velocity.rotate(rnum * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_movement_1 * 1.2
        asteroid2.velocity = new_movement_2 * 1.2
        







    
