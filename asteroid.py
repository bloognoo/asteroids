import pygame

from circleshape import CircleShape

from constants import LINE_WIDTH

class Asteroid(CircleShape) :
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", pygame.math.Vector2(self.position.x,self.position.y),self.radius, LINE_WIDTH)

    def update(self,dt:float) -> None:
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt


