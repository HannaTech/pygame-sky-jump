import pygame


class Jumper:

    _y = float(0)
    _x = float(0)
    _current_image = None

    def __init__(self, sj_game):
        self._screen = sj_game.screen
        self._screen_rect = sj_game.screen.get_rect()
        self._settings = sj_game.settings

        self._rect_width = self._settings.jumper_image_width
        self._rect_height = self._settings.jumper_image_height

        self.rect = pygame.Rect(Jumper._x, Jumper._y, self._rect_width, self._rect_height)

    @property
    def x(self):
        # x of left bottom angle
        return Jumper._x

    @x.setter
    def x(self, value):
        self.rect.x = value
        Jumper._x = float(value)

    @property
    def y(self):
        # y of left bottom angle
        return Jumper._y + self._rect_height

    @y.setter
    def y(self, value):
        self.rect.y = value - self._rect_height
        Jumper._y = float(value - self._rect_height)

    def print_jumper(self):
        self._screen.blit(Jumper._current_image, self.rect)
