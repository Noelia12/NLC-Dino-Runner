from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):


    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.obstacle_rect = self.image[self.type].get_rect()
        self.obstacle_rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.obstacle_rect.x -= game_speed
        if self.obstacle_rect.x < self.obstacle_rect.width:
            obstacles.pop()


    def draw(self, screen):
        screen.blit(self.image[self.type], self.obstacle_rect)
