import random

from dino_runner.components.Obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    def __init__(self, image, y_pos):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.obstacle_rect.y = y_pos
