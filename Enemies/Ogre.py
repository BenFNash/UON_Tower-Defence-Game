import pygame
from .Enemy import Enemy
import os

ogre_animation_imgs = []
ogre_attack_imgs = []

for i in range(23):
    if i < 10:
        add_str = '00' + str(i)
    else:
        add_str = '0' + str(i)
    ogre_animation_imgs.append(pygame.transform.scale(pygame.image.load(
        os.path.join('game_assets', 'Ogre', 'PNG', 'PNG Sequences',
                     'Walking', '0_Ogre_Walking_' + add_str + '.png')), (80, 80)))

    # ogre_attack_imgs.append(pygame.transform.scale(pygame.image.load(
    #   os.path.join('game_assets', 'Ogre', 'PNG', 'PNG Sequences',
    #               'Slashing', '0_Ogre_Slashing_' + add_str + '.png')), (80, 80)))


class Ogre(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = ogre_animation_imgs
        self.attack_imgs = ogre_attack_imgs
        self.speed = 0.25
        self.distance_multiplier = 10
