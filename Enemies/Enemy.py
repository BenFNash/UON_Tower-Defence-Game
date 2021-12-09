import pygame
import os
import random


class Enemy:

    def __init__(self):
        self.x = -40
        self.y = 115
        self.imgs = pygame.transform.scale(pygame.image.load(os.path.join(
            'game_assets', 'Goblin', 'PNG', 'PNG Sequences', 'Running', '0_Goblin_Running_000.png')), (64, 64))
        self.attack_imgs = pygame.transform.scale(pygame.image.load(os.path.join(
            'game_assets', 'Goblin', 'PNG', 'PNG Sequences', 'Running', '0_Goblin_Running_000.png')), (64, 64))
        self.animation_count = 0
        self.path_count = 0
        self.path = [[0, 115], [123, 115], [123, 458], [268, 458], [268, 288], [369, 288], [369, 185],
                     [296, 185], [296, 115], [440, 115], [440, 151], [615, 151], [615, 425], [713, 431]]
        self.speed = 1
        self.at_castle = False
        self.height_variance()
        self.distance_multiplier = 30

    def height_variance(self):
        height_random_multiplier = random.randint(1, 20)
        self.y -= height_random_multiplier
        for position in self.path:
            position[1] -= height_random_multiplier

    def modify_x(self, enemy_count):
        self.x -= random.randint(1, enemy_count * self.distance_multiplier)

    def draw(self, screen):
        if self.animation_count > len(self.imgs) - 1:
            self.animation_count = 0

        if self.at_castle:
            current_imgs = self.attack_imgs
        else:
            current_imgs = self.imgs

        screen.blit(current_imgs[self.animation_count], (self.x, self.y))
        self.move_enemy()
        self.animation_count += 1

    def move_enemy(self):
        if self.path_count < len(self.path):
            destination = self.path[self.path_count]
            if self.x != destination[0]:
                if destination[0] - self.x < 0:
                    self.x -= self.speed
                else:
                    self.x += self.speed

            if self.y != destination[1]:
                if destination[1] - self.y < 0:
                    self.y -= self.speed
                else:
                    self.y += self.speed

            if int(self.x) == destination[0] and int(self.y) == destination[1]:
                self.path_count += 1
        else:
            self.at_castle = True
