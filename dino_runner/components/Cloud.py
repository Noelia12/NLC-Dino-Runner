import random

from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD


class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.cloud_rect.y = random.randint(50, 100)

    def update(self, game_speed):
        self.cloud_rect.x -= game_speed
        if self.cloud_rect.x < -self.cloud_rect.width:
            self.cloud_rect.x = SCREEN_WIDTH

    def draw(self,screen):
        screen.blit(self.image,self.cloud_rect)
