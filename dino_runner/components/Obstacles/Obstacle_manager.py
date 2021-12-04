import pygame, random

from dino_runner.components.Obstacles.Pajaro import Pajaro
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.components.power_ups import hammer
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = random.randint(1, 3)
            # cactus = 3
            if cactus == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS, 328))
            if cactus == 2:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
            if cactus == 3:
                self.obstacles.append(Pajaro(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            # para acceder a la instancia de algo y dice self.algo,
            # reemplazamos el self por el nombre del objeto
            user_input = pygame.key.get_pressed()
            if game.player.dino_rect.colliderect(obstacle.obstacle_rect):
                if not game.player.shield:
                    if game.life_manager.life_counter() == 1:
                        pygame.time.delay(1000)
                        game.playing = False
                        game.death_account += 1
                        break
                    else:
                        game.life_manager.delete_life()
                self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
