import pygame
import os
import Enemies.Enemy as Enemy
import Enemies.Goblin as Goblin
import Enemies.Ogre as Ogre
import Enemies.Orc as Orc
import Player
import random
import Gui


class Game():

    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(
            'game_assets', 'Sounds', 'Kingdom of the Forest.mp3'))
        self.width = 960
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load(
            os.path.join('game_assets', 'map_final.png'))
        self.enemys = []
        self.castle_img = pygame.transform.scale(pygame.image.load(os.path.join(
            'game_assets', 'Castle', 'Asset 27.png')), (400, 400))
        self.difficulty_selected = 'easy'
        self.font = pygame.font.SysFont('arial', 50)
        self.player = Player.Player(self.difficulty_selected)
        self.enemy_count = 1
        self.wave_number = 0
        self.game_over = False
        self.paused = False
        self.currency = 0

    def play(self):
        playing = True
        clock = pygame.time.Clock()
        pygame.mixer.music.play(-1)
        while playing:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False

                pos_x, pos_y = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    if Gui.pause_play_action(pos_x, pos_y):
                        self.paused = not self.paused
                    Gui.exit_action(pos_x, pos_y)
                    Gui.audio_button_action(pos_x, pos_y)
            if not self.game_over:
                if not self.paused:

                    if self.enemys == []:
                        self.new_wave()

                    self.draw()

                    for enemy in self.enemys:
                        enemy.draw(self.window)
                        if enemy.at_castle:
                            self.enemys.remove(enemy)
                            self.player.lives -= 1
                            if self.player.lives < 1:
                                self.game_over = True

                    Gui.archer_tower.action(pos_x, pos_y)
                    Gui.wizard_tower.action(pos_x, pos_y)
                else:
                    self.pause_menu()
                    Gui.draw_interface(self.window, self.player.lives,
                                       self.wave_number, self.currency)
            else:
                self.draw()
            pygame.display.update()

        pygame.quit()

    def draw(self):
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.castle_img, ((748, 160)))
        lives_surface = self.font.render('Lives: ' +
                                         str(self.player.lives), False, pygame.Color('white'))
        self.window.blit(lives_surface, (700, 160))
        if self.player.lives < 9:
            self.castle_img = pygame.transform.scale(pygame.image.load(os.path.join(
                'game_assets', 'Castle', 'Asset 28.png')), (400, 400))

        if self.game_over:
            self.game_over_surface = self.font.render(
                f'You Lose!.... You survived {self.wave_number} waves', False, pygame.Color('white'))
            self.window.blit(self.game_over_surface,
                             (self.width / 2 - 300, self.height / 2))
            self.castle_img = pygame.transform.scale(pygame.image.load(os.path.join(
                'game_assets', 'Castle',  'Asset 29.png')), (400, 400))

        Gui.draw_interface(self.window, self.player.lives,
                           self.wave_number, self.currency)

    def new_wave(self):
        self.enemy_count = 0
        self.wave_number += 1
        while self.enemy_count < 30:
            if self.enemy_count < 10:
                self.enemys.append(Goblin.Goblin())
                self.enemy_count += 1
            elif self.enemy_count < 20:
                self.enemys.append(Ogre.Ogre())
                self.enemy_count += 1
            else:
                self.enemys.append(Orc.Orc())
                self.enemy_count += 1

        for enemy in self.enemys:
            enemy.modify_x(self.enemy_count)

    def pause_menu(self):
        text_surface = self.font.render(
            f'Game Paused, You are on wave {self.wave_number}', False, pygame.Color('white'))
        self.window.blit(text_surface, (self.width / 2 - 400, self.height / 2))
