import pygame


class GameStats:

    def __init__(self, sj_game):
        self.settings = sj_game.settings
        self._game_active = False
        self.score = 0

    @property
    def game_active(self):
        return self._game_active

    @game_active.setter
    def game_active(self, value):
        self._game_active = value
        pygame.mouse.set_visible(not value)