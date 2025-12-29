import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        a = self.position + pygame.Vector2(0, 1) * self.radius
        b = self.position + pygame.Vector2(0, 1) * self.radius
        c = self.position +pygame.Vector2(0, 1) * self.radius 
        pygame.draw.polygon(screen,"WHITE", [a,b,c] ,LINE_WIDTH)
    
    def update(self, dt):
       self.position+=self.velocity * dt

        



    
