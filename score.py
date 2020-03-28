import pygame.font


class Score:

    def __init__(self, sj_game):
        self.screen = sj_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sj_game.settings

        self.width, self.height = 200, 100
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.msg_image = None
        self.msg_image_rect = None

    def prep_msg(self, msg):
        self.msg_image = self.font.render('Score : ' + str(msg), True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()

    def draw_score(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

