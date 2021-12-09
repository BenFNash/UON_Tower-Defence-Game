import pygame
import os


class Constants:
    pygame.font.init()
    BACKGROUND_IMAGE = pygame.image.load(
        os.path.join('game_assets', 'map_final.png'))
    MAIN_MENU_MUSIC = os.path.join(
        'game_assets', 'main_menu', 'critical_tower_defense_theme.mp3')
    FONT = os.path.join('game_assets', 'main_menu', 'Retro.ttf')

    def text_format(message, text_font, text_size, text_color):
        text_color = pygame.Color(text_color)
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_color)
        return new_text

    TITLE_TEXT = text_format('Tower Defence', FONT, 120, 'black')
    PLAY_TEXT = text_format('Play', FONT, 69, 'white')
    SOUND_TEXT = text_format('Sound', FONT, 69, 'white')
    HELP_TEXT = text_format('Help', FONT, 69, 'white')
    ABOUT_TEXT = text_format('About', FONT, 69, 'white')
    EXIT_TEXT = text_format('Exit', FONT, 69, 'white')
    TITLE_TEXT.set_colorkey(pygame.Color('blue'))
    WIN_WIDTH = 960
    WIN_HEIGHT = 720
