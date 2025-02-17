import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,width=2)
    
    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        blue_angle = random.uniform(20,50)
        blue_velocity = self.velocity.rotate(blue_angle)
        red_velocity = self.velocity.rotate(-blue_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        blue_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        red_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        blue_asteroid.velocity = blue_velocity*1.2
        red_asteroid.velocity = red_velocity*1.2
        



        
        
    


