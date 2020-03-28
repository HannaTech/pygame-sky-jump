from jumper import Jumper


class JumperMain(Jumper):

    def __init__(self, sj_game):
        super().__init__(sj_game)

        # start position
        self.x = self._screen_rect.width/2 - self._rect_width/2
        self.y = self._screen_rect.height

        # y coordinate of jump start point
        self.jump_start_y = self.y

        # -1 - moving left, 1 - moving right, 0 - no movement along horizontal axis
        self.direction_h = 0
        # -1 - moving up, 1 - moving down
        self.direction_v = -1

        self.stats = sj_game.stats

    def _get_image(self):
        if self.direction_h == 1 and self.direction_v == -1:
            return self._settings.jumper_image_right_up
        elif self.direction_h == 1 and self.direction_v == 1:
            return self._settings.jumper_image_right_down
        elif self.direction_h == -1 and self.direction_v == -1:
            return self._settings.jumper_image_left_up
        elif self.direction_h == -1 and self.direction_v == 1:
            return self._settings.jumper_image_left_down
        else:
            return self._settings.jumper_image_right_down

    def _update_v_direction(self):
        if self.y <= self.jump_start_y - self._settings.jump_height or self.rect.y == 0:
            self.direction_v = 1
        elif self.y >= self._screen_rect.bottom:
            self.direction_v = -1
            self.jump_start_y = self._screen_rect.height

    def update(self):
        self._update_v_direction()
        self.y += self.direction_v * self._settings.jump_v_speed
        self.x += self.direction_h * self._settings.jump_h_speed
        Jumper._current_image = self._get_image()
        if self.y >= self._settings.screen_height:
            self.stats.game_active = False

    def border_is_crossed(self):
        if self.x < 0 or self.x + self._rect_width > self._screen_rect.right:
            return True
        else:
            return False



