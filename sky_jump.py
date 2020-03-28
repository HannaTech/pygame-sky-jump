import pygame
from settings import Settings
import sys
from jumper_main import JumperMain
from jumper_clone import JumperClone
from cloud import Cloud
import random
import math
from button import Button
from stats import GameStats
from score import Score


class SkyJump:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sky Jumper')
        self.jumper = JumperMain(self)
        self.jumper_copy = JumperClone(self)
        self.clouds = pygame.sprite.Group()

        self.cloud_next_y = None
        self._cloud_count = math.ceil(self.settings.screen_height / (self.settings.cloud_image_height +
                                                                     self.settings.cloud_distance))

        self.play_button = Button(self, 'Play')
        self.score = Score(self)

    def run_game(self):

        while True:
            self.screen.fill(self.settings.screen_bgcolor)
            if not self.stats.game_active:
                self.play_button.draw_button()
                self._check_events()
            else:
                self._check_events()
                self._update_game()
            pygame.display.flip()

    def _update_game(self):
        self.jumper.update()
        self._update_clouds()
        self.clouds.draw(self.screen)
        if self.jumper.border_is_crossed():
            self.jumper_copy.update()
            self._check_collision(self.jumper_copy)
            self.jumper_copy.print_jumper()
        self._check_collision(self.jumper)
        self.jumper.print_jumper()
        self.score.prep_msg(self.stats.score)
        self.score.draw_score()

    def _check_collision(self, jumper):
        cloud = pygame.sprite.spritecollideany(jumper, self.clouds)

        if cloud and self.jumper.direction_v == 1 and int(self.jumper.y) == int(cloud.y) + 1:
            if (jumper.rect.x + 1/3*self.settings.jumper_image_width <= cloud.x + self.settings.cloud_image_width) \
              and (jumper.rect.x + 2/3*self.settings.jumper_image_width >= cloud.x):
                self.jumper.jump_start_y = self.jumper.y
                self.jumper.direction_v = -1
                self.stats.score = max(cloud.score, self.stats.score)

    def _update_clouds(self):
        self.clouds.update()
        cloud_count = len(self.clouds)
        for cloud in self.clouds.copy():
            if cloud.y > self.settings.screen_height:
                self.clouds.remove(cloud)
            if self._cloud_count == cloud_count and \
                    cloud.y + self.settings.cloud_image_height >= self.settings.screen_height:
                self.clouds.add(self._create_cloud(-self.settings.cloud_image_height))

    def _create_clouds(self):
        i = self.settings.screen_height - self.settings.cloud_image_height
        while i > 0:
            cloud = self._create_cloud(i)
            self.clouds.add(cloud)
            i -= self.settings.cloud_distance + self.settings.cloud_image_height
        self.cloud_next_y = i

    def _create_cloud(self, y):
        x = random.randint(0, self.settings.screen_width - self.settings.cloud_image_width)
        return Cloud(self, x, y)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True
            self._init_game()

    def _init_game(self):
        Cloud.cloud_max_score = 0
        self.stats.score = 0
        self.clouds.empty()
        self._create_clouds()
        self.jumper.x = self.settings.screen_width / 2 - self.settings.jumper_image_width / 2
        self.jumper.y = self.settings.screen_height / 2

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.jumper.direction_h = 1
        elif event.key == pygame.K_LEFT:
            self.jumper.direction_h = -1
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.jumper.direction_h = 0


if __name__ == '__main__':
    sj_game = SkyJump()
    sj_game.run_game()
