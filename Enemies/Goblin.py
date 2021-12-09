import pygame
from .Enemy import Enemy
import os

goblin_animation_imgs = []
goblin_attack_imgs = []
image_types = ['0_Goblin_Running_', '0_Goblin_Slashing_']
for i in range(10):
    if i < 10:
        add_str = '00' + str(i)
    else:
        add_str = '0' + str(i)

    goblin_animation_imgs.append(pygame.transform.scale(pygame.image.load(
        os.path.join('game_assets', 'Goblin', 'PNG', 'PNG Sequences',
                     'Running', '0_Goblin_Running_' + add_str + '.png')), (50, 50)))

    goblin_attack_imgs.append(pygame.transform.scale(pygame.image.load(
        os.path.join('game_assets', 'Goblin', 'PNG', 'PNG Sequences',
                     'Slashing', '0_Goblin_Slashing_' + add_str + '.png')), (50, 50)))


class Goblin(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = goblin_animation_imgs
        self.attack_imgs = goblin_attack_imgs
