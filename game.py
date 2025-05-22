import pygame
from menus import MainMenu, OptionsMenu
from assets import Assets
from subjects_menu import SubjectsMenu
from game_screen import GameScreen

class Game:
    # Main game controller class
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Screen setup
        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Code Milionário")

        # Load assets and menus
        self.assets = Assets()
        self.main_menu = MainMenu(self.screen, self.assets)
        self.options_menu = OptionsMenu(self.screen, self.assets)
        self.subjects_menu = SubjectsMenu(self.screen, self.assets)
        self.game_screen = GameScreen(self.screen, self.assets)
        self.running = True

    def run(self):
        # Main game loop
        while self.running:
            self.screen.blit(self.assets.background, (0, 0))
            # Center logo at top
            logo_x = (self.SCREEN_WIDTH - self.assets.logo_img.get_width()) // 2
            self.screen.blit(self.assets.logo_img, (logo_x, 30))

            if self.main_menu.update():
                self.assets.click_sound.play()
                self.subjects_menu.show()
                if self.subjects_menu.start_clicked:
                    self.game_screen.show()

            if self.main_menu.options_clicked:
                self.assets.click_sound.play()
                pygame.time.wait(150)  # Debounce clicks
                self.options_menu.show()
                self.main_menu.options_clicked = False

            if self.main_menu.exit_clicked:
                self.assets.click_sound.play()
                print("Exit clicked!")
                self.running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()