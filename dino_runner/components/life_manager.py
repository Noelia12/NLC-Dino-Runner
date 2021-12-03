from dino_runner.components.life import Life

class LifeManager:
    def __init__(self):
        self.life_list = []

    def new_lifes(self):
        self.life_list = []
        total_lifes = 3 #Cantidad de vidas
        pos_x = 30

        for life in range(0, total_lifes):
            self.life_list.append(Life(pos_x))
            pos_x += 30 #Distancia entre vidas

    def draw(self, screen):
        for life in self.life_list:
            life.draw(screen)

    def delete_life(self):
        self.life_list.pop()

    def life_counter(self):
        return len(self.life_list)
