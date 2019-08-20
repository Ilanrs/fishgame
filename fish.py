import  pygame, random

class Fish:
    def __init__(self, pos):
        self.image = pygame.image.load("fish.png")
        scale = random.randint(1, 5) * 10
        self.image = pygame.transform.smoothscale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randit(2, 5))

        rotation = random.randint(0, 360)
        self.speed.rotate_ip(rotation)
        self.image = pygame.transform.rotate(self.image, 180 - rotation)