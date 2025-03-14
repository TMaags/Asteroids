import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from circleshape import CircleShape
from Shot import Shot


class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        
        #rotate left when 'a' is pressed
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        #rotate right when 'd' is pressed
        if keys[pygame.K_d]:
            self.rotate(dt)

        #move forward when 'w' is pressed
        if keys[pygame.K_w]:
            self.move(dt)
        
        #move backward when 's' is pressed
        if keys[pygame.K_s]:
            self.move(dt * -1)

        #shoot when 'spacebar' is pressed
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer += PLAYER_SHOT_COOLDOWN

        #reduce cooldown if spacebar isnt pressed
        if self.timer > 0:
            self.timer -= dt
        
        #if the timer is less than 0 reset it to 0
        if self.timer < 0:
            self.timer = 0
        


        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity.rotate_ip(self.rotation)
        shot.velocity *= PLAYER_SHOT_SPEED
        return shot