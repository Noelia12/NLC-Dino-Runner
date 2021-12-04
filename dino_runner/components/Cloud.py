import random

from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD


class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = 0
        self.cloud_rect.y = random.randint(50, 200)

    def update(self, game_speed):
        self.cloud_rect.x -= game_speed
        if self.cloud_rect.x < -self.cloud_rect.width:
            self.cloud_rect.x = random.randint(10,800) + SCREEN_WIDTH
            self.cloud_rect.y = random.randint(30, 200)

    def draw(self,screen):
        screen.blit(self.image, self.cloud_rect)
