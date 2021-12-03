import random

from dino_runner.components.Obstacles.obstacle import Obstacle


class Pajaro(Obstacle):

    def __init__(self, image):
        self.index = 0
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.obstacle_rect.y = 50*random.randint(4, 6)

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.obstacle_rect)
        self.index += 1
