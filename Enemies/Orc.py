import pygame
from .Enemy import Enemy
import os

orc_animation_imgs = []
orc_attack_imgs = []

for i in range(10):
    if i < 10:
        add_str = '00' + str(i)
    else:
        add_str = '0' + str(i)
    orc_animation_imgs.append(pygame.transform.scale(pygame.image.load(
        os.path.join('game_assets', 'Orc', 'PNG', 'PNG Sequences',
                     'Running', '0_Orc_Running_' + add_str + '.png')), (64, 64)))

    orc_attack_imgs.append(pygame.transform.scale(pygame.image.load(
        os.path.join('game_assets', 'Orc', 'PNG', 'PNG Sequences',
                     'Slashing', '0_Orc_Slashing_' + add_str + '.png')), (64, 64)))


class Orc(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = orc_animation_imgs
        self.attack_imgs = orc_attack_imgs
        self.speed = 0.5
        self.distance_multiplier = 20
