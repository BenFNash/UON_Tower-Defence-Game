import pygame
from pygame.constants import MOUSEBUTTONDOWN
import os
import Game
import Constants

k = Constants.Constants()

# initializations from the pygame module #
pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.music.load(k.MAIN_MENU_MUSIC)
# you can change the volume of the music in this function
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

# constants #
WIN_HEIGHT = 720
WIN_WIDTH = 960

# images #
background_image = pygame.image.load(
    os.path.join('game_assets', 'map_final.png'))

# display settings #
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
title = 'Sample Title'  # you can change this variable for the title of the window
pygame.display.set_caption(title)

# colors #
white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 60, 60)
blue = (60, 92, 250)
green = (47, 206, 47)

# global variables #
now_time = 0
toggle_music = True


def main():

    # variables #
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    font = os.path.join('game_assets', 'main_menu', 'Retro.ttf')
    mouse = pygame.mouse

    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText

    def text_hover(rect, nr):
        if mouse.get_pos()[0] > WIN_WIDTH/2 - (rect[2]/2) and mouse.get_pos()[0] < WIN_WIDTH/2 + (rect[2]/2) and mouse.get_pos()[1] > WIN_HEIGHT/10 * nr - (rect[3]/2) and mouse.get_pos()[1] < WIN_HEIGHT/10 * nr + (rect[3]/2):
            return True

        return False

    def redraw_window():

        global toggle_music, now_time

        win.fill((0, 0, 0))

        win.blit(k.BACKGROUND_IMAGE, (0, 0))

        title_text = text_format('Tower Defense', font, 120, black)
        play_text = text_format('Play', font, 69, white)
        sound_text = text_format('Sound', font, 69, white)
        help_text = text_format('Help', font, 69, white)
        about_text = text_format('About', font, 69, white)
        exit_text = text_format('Exit', font, 69, white)

        title_rect = k.TITLE_TEXT.get_rect(
            center=(k.TITLE_TEXT.get_width()/2, k.TITLE_TEXT.get_height()/2))
        title_rect.x, title_rect.y = WIN_WIDTH/2 - \
            (title_rect[2]/2), WIN_HEIGHT/10 - (title_rect[3]/2)

        play_rect = k.PLAY_TEXT.get_rect(
            center=(k.PLAY_TEXT.get_width()/2, k.PLAY_TEXT.get_height()/2))
        play_rect.x, play_rect. y = WIN_WIDTH/2 - \
            (play_rect[2]/2), WIN_HEIGHT/10 * 2.5 - (play_rect[3]/2)

        sound_rect = sound_text.get_rect(
            center=(sound_text.get_width()/2, sound_text.get_height()/2))
        sound_rect.x, sound_rect. y = WIN_WIDTH/2 - \
            (sound_rect[2]/2), WIN_HEIGHT/10 * 4 - (sound_rect[3]/2)

        help_rect = help_text.get_rect(
            center=(help_text.get_width()/2, help_text.get_height()/2))
        help_rect.x, help_rect. y = WIN_WIDTH/2 - \
            (help_rect[2]/2), WIN_HEIGHT/10 * 5.5 - (help_rect[3]/2)

        about_rect = about_text.get_rect(
            center=(about_text.get_width()/2, about_text.get_height()/2))
        about_rect.x, about_rect. y = WIN_WIDTH/2 - \
            (about_rect[2]/2), WIN_HEIGHT/10 * 7 - (about_rect[3]/2)

        exit_rect = exit_text.get_rect(
            center=(exit_text.get_width()/2, exit_text.get_height()/2))
        exit_rect.x, exit_rect. y = WIN_WIDTH/2 - \
            (exit_rect[2]/2), WIN_HEIGHT/10 * 8.5 - (exit_rect[3]/2)

        if text_hover(play_rect, 2.5):
            play_text = text_format('Play', font, 69, blue)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Game.Game().play()
            mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif text_hover(sound_rect, 4):
            sound_text = text_format('Sound', font, 69, blue)
            mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif text_hover(help_rect, 5.5):
            help_text = text_format('Help', font, 69, blue)
            mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif text_hover(about_rect, 7):
            about_text = text_format('About', font, 69, blue)
            mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif text_hover(exit_rect, 8.5):
            exit_text = text_format('Exit', font, 69, blue)
            mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        win.blit(title_text, (WIN_WIDTH/2 -
                 (title_rect[2]/2), WIN_HEIGHT/10 - (title_rect[3]/2)))
        win.blit(play_text, (WIN_WIDTH/2 -
                 (play_rect[2]/2), WIN_HEIGHT/10 * 2.5 - (play_rect[3]/2)))
        print(f'play rect {play_rect}')
        win.blit(sound_text, (WIN_WIDTH/2 -
                 (sound_rect[2]/2), WIN_HEIGHT/10 * 4 - (sound_rect[3]/2)))
        print(f'sound Rect: {sound_rect[2]}')
        win.blit(help_text, (WIN_WIDTH/2 -
                 (help_rect[2]/2), WIN_HEIGHT/10 * 5.5 - (help_rect[3]/2)))
        print(f'help rect: {help_rect[2]}')
        win.blit(about_text, (WIN_WIDTH/2 -
                 (about_rect[2]/2), WIN_HEIGHT/10 * 7 - (about_rect[3]/2)))
        print(f'about rect {about_rect[2]}')
        win.blit(exit_text, (WIN_WIDTH/2 -
                 (exit_rect[2]/2), WIN_HEIGHT/10 * 8.5 - (exit_rect[3]/2)))

        if mouse.get_pressed()[0] and text_hover(sound_rect, 4) and (pygame.time.get_ticks() - now_time) > 300:
            if toggle_music:
                now_time = pygame.time.get_ticks()
                toggle_music = False
                pygame.mixer.music.pause()
            else:
                now_time = pygame.time.get_ticks()
                toggle_music = True
                pygame.mixer.music.unpause()

        print(pygame.time.get_ticks() - now_time)

        pygame.display.update()

    while run:

        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        redraw_window()

        # close the window/game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_ESCAPE]:
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
