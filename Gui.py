import os
import pygame

""" Set constants """
black = (0, 0, 0)
music_on = True
Pause = False
""" Load in image resources """
guiPanel = pygame.image.load(os.path.join('game_assets', 'GUI', 'panel.png'))
guiLives = pygame.image.load(os.path.join('game_assets', 'GUI', 'lives.png'))
guiCurrency = pygame.image.load(
    os.path.join('game_assets', 'GUI', 'coin.png'))
guiCurrencySmall = pygame.image.load(
    os.path.join('game_assets', 'GUI', 'coin_small.png'))
guiSoundOff = pygame.image.load(os.path.join(
    'game_assets', 'GUI', 'black_music_off.png'))
guiSoundOn = pygame.image.load(os.path.join(
    'game_assets', 'GUI', 'black_music_on.png'))
guiExit = pygame.image.load(os.path.join(
    'game_assets', 'GUI', 'black_exit.png'))
guiPause = pygame.image.load(os.path.join(
    'game_assets', 'GUI', 'black_pause.png'))
guiPlay = pygame.image.load(os.path.join(
    'game_assets', 'GUI', 'black_play.png'))
guiTowerWizard = pygame.image.load(
    os.path.join('game_assets', 'GUI', 'wizard.png'))
guiTowerArcher = pygame.image.load(
    os.path.join('game_assets', 'GUI', 'archer.png'))


""" Main panel for game info """


class Interface_panel:

    def draw_info_panel(screen, lives, waveCount, currency):
        """ Set text colour, font and text for Information Panel """
        font = pygame.font.SysFont(None, 40)
        guiLivesLabel = font.render(str(lives), True, black)
        guiCurrencyLabel = font.render(str(currency), True, black)
        guiWaveLabel = font.render('Wave:', True, black)
        guiWaveCount = font.render(str(waveCount), True, black)

        """ Draw in each of these elements """
        screen.blit(guiPanel, (15, 15))
        screen.blit(guiLives, (30, 30))
        screen.blit(guiLivesLabel, (75, 32))
        screen.blit(guiWaveLabel, (262, 32))
        screen.blit(guiWaveCount, (350, 32))
        screen.blit(guiCurrency, (30, 70))
        screen.blit(guiCurrencyLabel, (75, 75))


""" Create a standard button with two imaages to toggle """


class Button:

    def __init__(self, x, y, img1, img2):
        self.x = x
        self.y = y
        self.images = [img1, img2]
        self.c = 0
        self.width = img1.get_width()
        self.height = img2.get_height()

    def onSpace(self):
        self.c = (self.c + 1) % len(self.images)

    def get_image(self):
        return self.images[self.c]

    def draw_button(self, screen):
        screen.blit(self.images[self.c], (self.x, self.y))


""" Add new type of button, different to button for towers """


class Tower_Button:

    def __init__(self, x, y, image, cost):
        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.cost = cost

    def draw_button(self, screen, currency):
        if currency >= self.cost:
            font = pygame.font.SysFont(None, 35)
            screen.blit(self.image, (self.x, self.y))
            price_y = self.y + self.height + 5
            price_tag = font.render(str(self.cost), True, black)
            screen.blit(guiCurrencySmall, (self.x, price_y))
            screen.blit(price_tag, (self.x + 30, price_y+2))

    def action(self, pos_x, pos_y):
        if pos_x >= self.x and pos_x <= self.x + self.width:
            if pos_y >= self.y and pos_y <= self.y + self.height:
                print("BUILD TOWER")

                # CURRENCY MUST BE UPDATED HERE


""" Function to check given mouse position is in button clickable area """


def check_click_area(button_name, pos_x, pos_y):
    if pos_x >= button_name.x and pos_x <= button_name.x + button_name.width:
        if pos_y >= button_name.y and pos_y <= button_name.y + button_name.height:
            return True


""" Create instances of different control buttons"""
pause_play_button = Button(260, 60, guiPause, guiPlay)
audio_button = Button(310, 60, guiSoundOn, guiSoundOff, )
exit_button = Button(360, 60, guiExit, guiExit)


""" Define actions for each control button as a function """


def audio_button_action(pos_x, pos_y):
    if check_click_area(audio_button, pos_x, pos_y):
        audio_button.onSpace()
        global music_on
        if music_on == True:
            pygame.mixer.music.pause()
            music_on = False
            print("false")
        else:
            music_on = True
            pygame.mixer.music.unpause()
            print("true")


def pause_play_action(pos_x, pos_y):
    if check_click_area(pause_play_button, pos_x, pos_y):
        pause_play_button.onSpace()
        return True


def exit_action(pos_x, pos_y):
    if check_click_area(exit_button, pos_x, pos_y):
        pygame.quit()


""" Create instances of different tower buttons """
archer_tower = Tower_Button(60, 600, guiTowerArcher, 300)
wizard_tower = Tower_Button(160, 600, guiTowerWizard, 400)


""" One simple function to pass to the main game file """


def draw_interface(screen, lives, waveCount, currency):
    # Top panel
    Interface_panel.draw_info_panel(screen, lives, waveCount, currency)
    audio_button.draw_button(screen)
    exit_button.draw_button(screen)
    pause_play_button.draw_button(screen)

    archer_tower.draw_button(screen, currency)
    wizard_tower.draw_button(screen, currency)


""" 

ADD THIS TO DRAW IN GAME.Py




Add the following within the main game loop:

pos_x, pos_y = pygame.mouse.get_pos()
if event.type == pygame.MOUSEBUTTONUP:

     if Gui.pause_play_action(pos_x, pos_y):
             self.paused = not self.paused
     Gui.archer_tower.action(pos_x, pos_y)
     Gui.wizard_tower.action(pos_x, pos_y)
     Gui.exit_action(pos_x, pos_y)
     Gui.audio_button_action(pos_x, pos_y)
       

"""
