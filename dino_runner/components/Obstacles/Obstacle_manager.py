import pygame

from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            #para acceder a la instancia de algo y dice self.algo,
            #reemplazamos el self por el nombre del objeto
            if game.player.dino_rect.colliderect(obstacle.obstacle_rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)