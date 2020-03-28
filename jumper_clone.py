from jumper import Jumper


class JumperClone(Jumper):

    def __init__(self, sj_game):
        super().__init__(sj_game)

    def update(self):

        # jumper completely out of borders
        if Jumper._x + self._rect_width < 0 or Jumper._x > self._screen_rect.right:
            Jumper._x = self.rect.x

        if Jumper._x + self._rect_width > self._screen_rect.width:
            self.rect.x = Jumper._x - self._screen_rect.width
        elif Jumper._x < 0:
            self.rect.x = Jumper._x + self._screen_rect.width

        self.rect.y = Jumper._y


