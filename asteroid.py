import pygame
import random

from logger import log_event 

from circleshape import CircleShape

from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape) :
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", pygame.math.Vector2(self.position.x,self.position.y),self.radius, LINE_WIDTH)

    def update(self,dt:float) -> None:
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self) -> None :
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return # small asteroid
        else :
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = self.velocity.rotate(angle)
            asteroid1.velocity.scale_to_length(asteroid1.velocity.magnitude() * 1.2)
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2.velocity = self.velocity.rotate(-angle)
            asteroid2.velocity.scale_to_length(asteroid2.velocity.magnitude() * 1.2)
