from dino_runner.components.life import Life
from dino_runner.utils.constants import SCREEN_WIDTH


class LifeManager:

    def __init__(self):
        self.life_list = []

    def new_lifes(self):
        self.life_list = []
        total_lifes = 3 #Cantidad de vidas
        pos_x = 1010

        for life in range(0, total_lifes):
            life = Life(pos_x)
            self.life_list.append(life)
            pos_x -= life.image.get_width()
            # Distancia entre vidas

    def draw(self, screen):
        for life in self.life_list:
            life.draw(screen)

    def delete_life(self):
        self.life_list.pop()

    def life_counter(self):
        return len(self.life_list)
