import pygame
from pygame.sprite import Sprite


class Cloud(Sprite):

    cloud_max_score = 0

    def __init__(self, sj_game, x, y):
        super().__init__()
        self._screen = sj_game.screen
        self._screen_rect = sj_game.screen.get_rect()
        self._settings = sj_game.settings

        self._rect_width = self._settings.cloud_image_width
        self._rect_height = self._settings.cloud_image_height

        self.image = self._settings.cloud_image

        self._x = float(x)
        self._y = float(y)

        self.rect = pygame.Rect(x, y, self._rect_width, self._rect_height)

        Cloud.cloud_max_score += 1
        self.score = Cloud.cloud_max_score

    @property
    def x(self):
        # x of left top angle
        return self._x

    @x.setter
    def x(self, value):
        self.rect.x = value
        self._x = float(value)

    @property
    def y(self):
        # y of left top angle
        return self._y

    @y.setter
    def y(self, value):
        self.rect.y = value
        self._y = float(value)

    def update(self):
        self.y += self._settings.cloud_speed


