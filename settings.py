import pygame


class Settings:

    def __init__(self):
        self.screen_height = 700
        self.screen_width = 900
        self.screen_bgcolor = (115, 194, 251)

        self.jump_height = 150
        self.jump_v_speed = 0.8
        self.jump_h_speed = 1

        self.jumper_image_left_down = pygame.image.load('images/jumper_left_down.bmp')
        self.jumper_image_left_up = pygame.image.load('images/jumper_left_up.bmp')
        self.jumper_image_right_down = pygame.image.load('images/jumper_right_down.bmp')
        self.jumper_image_right_up = pygame.image.load('images/jumper_right_up.bmp')

        self.jumper_image_width = self.jumper_image_left_down.get_rect().width
        self.jumper_image_height = self.jumper_image_left_down.get_rect().height

        self.cloud_image = pygame.image.load('images/cloud.bmp')

        self.cloud_image_width = self.cloud_image.get_rect().width
        self.cloud_image_height = self.cloud_image.get_rect().height

        self.cloud_distance = 20
        self.cloud_speed = 0.2


