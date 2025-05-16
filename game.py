import pygame
from menus import MainMenu, OptionsMenu
from assets import Assets

# Main Game class to control the application flow
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Game screen setup
        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Code Milionário")

        # Load assets and menus
        self.assets = Assets()
        self.main_menu = MainMenu(self.screen, self.assets)
        self.options_menu = OptionsMenu(self.screen, self.assets)
        self.running = True

    # Main game loop
    def run(self):
        while self.running:
            self.screen.blit(self.assets.background, (0, 0))
            self.screen.blit(self.assets.logo_img, ((self.SCREEN_WIDTH - self.assets.logo_img.get_width()) // 2, 30))

            if self.main_menu.update():
                self.assets.click_sound.play()
                print("Start clicked!")

            if self.main_menu.options_clicked:
              self.assets.click_sound.play()
              pygame.time.wait(150)  # Wait for 150ms to avoid double click
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