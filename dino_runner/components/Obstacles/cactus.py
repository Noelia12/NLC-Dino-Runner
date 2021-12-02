import random

from dino_runner.components.Obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    Y_POS = 333

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.obstacle_rect.y = self.Y_POS
