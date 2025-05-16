import pygame

# Asset manager to centralize image and sound loading
class Assets:
    def __init__(self):
        self.load_images()
        self.load_sounds()
        self.load_fonts()

    def load_images(self):
        self.background = pygame.image.load("images/background.png").convert()
        self.logo_img = pygame.image.load("images/logo.png").convert_alpha()

        self.start_img = self.load_scaled("images/botao_iniciar.png")
        self.options_img = self.load_scaled("images/botao_opcoes.png")
        self.exit_img = self.load_scaled("images/botao_sair.png")
        self.music_img = self.load_scaled("images/botao_musica.png")
        self.sound_img = self.load_scaled("images/botao_som.png")
        self.back_img = self.load_scaled("images/botao_sair.png")
        self.fullscreen_img = self.load_scaled("images/botao_tela.png")

        self.checkbox_on = pygame.transform.scale(pygame.image.load("images/checkbox_on.png"), (60, 60))
        self.checkbox_off = pygame.transform.scale(pygame.image.load("images/checkbox_off.png"), (60, 60))

    def load_sounds(self):
        pygame.mixer.music.load("assets/mainmenu.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        self.click_sound = pygame.mixer.Sound("assets/button.mp3")
        self.click_sound.set_volume(0.1)

    def load_fonts(self):
        self.font = pygame.font.Font("assets/Font.ttf", 74)
        self.volume_font = pygame.font.Font("assets/Font.ttf", 48)

    def load_scaled(self, path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, (225, 90))