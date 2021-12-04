import pygame

from dino_runner.components.Cloud import Cloud
from dino_runner.components.Obstacles.Obstacle_manager import ObstacleManager
from dino_runner.components.life_manager import LifeManager
from dino_runner.components.power_ups import hammer
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.text_utils import get_score_element, get_centered_message
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DINO_START
from dino_runner.components.dinosaurio import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.hammer = Hammer()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()
        self.life_manager = LifeManager()
        self.points = 0
        self.running = True
        self.death_account = 0

    def run(self):
        self.create_components()
        # Game loop: events - update - draw
        self.playing = True
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points,self.player)
        self.life_manager.new_lifes()

    def execute(self):
        # mostrar menu
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(self.game_speed-4)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud.draw(self.screen)
        self.score()
        self.player.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.life_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)
        self.player.check_inv(self.screen)

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements(self.death_account)
        # actualizar la vista del juego
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_account=0):
        # variables opcionales:
        half_sh = SCREEN_HEIGHT//2
        half_sw = SCREEN_WIDTH//2
        # print('muertes {}'.format(self.death_account))
        text, text_rect = get_centered_message('Press any key to star')
        self.screen.blit(text, text_rect)
        self.screen.blit(DINO_START, (500, 150))

        if not death_account == 0:
            death, death_rect = get_centered_message('Your score : {}'.format(self.points), half_sw, half_sh + 100)
            self.screen.blit(death, death_rect)
            death, death_rect = get_centered_message('Death : {}'.format(self.death_account), half_sw, half_sh + 50)
            self.screen.blit(death, death_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                self.run()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
