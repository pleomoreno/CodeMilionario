import pygame
from button import Button

class GameScreen:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.tip_visible = False
        self.running = True

        # Botões de resposta
        self.answer_buttons = {
            "A": Button(40, 160, assets.answer_a_img),
            "B": Button(40, 240, assets.answer_b_img),
            "C": Button(40, 320, assets.answer_c_img),
            "D": Button(40, 400, assets.answer_d_img),
        }

        # Botões de ajuda
        self.help_buttons = {
            "pular": Button(730, 430, assets.botao_pular0_img),
            "dica": Button(840, 430, assets.botao_dica0_img),
            "eliminar": Button(950, 430, assets.botao_eliminar0_img),
        }

        # Vidas das ajudas (3 para cada)
        self.help_lives = {
            "pular": 3,
            "dica": 3,
            "eliminar": 3,
        }

    def show(self):
        while self.running:
            self.screen.blit(self.assets.background, (0, 0))
            self.screen.blit(self.assets.question_box_img, (100, 40))

            # Texto da pergunta
            question_text = self.assets.font.render("1. Qual é a saída de print(2 ** 3)?", True, (255, 255, 255))
            self.screen.blit(question_text, (130, 60))

            # Desenhar botões de resposta
            for button in self.answer_buttons.values():
                button.draw(self.screen)

            # Tip box (só aparece se ativar a dica)
            if self.tip_visible:
                self.screen.blit(self.assets.tip_box_img, (580, 140))
                tip_text = self.assets.small_font.render("Dica: É exponenciação", True, (255, 255, 255))
                self.screen.blit(tip_text, (600, 160))

            # Botões de ajuda
            for name, button in self.help_buttons.items():
                if button.draw(self.screen):
                    if self.help_lives[name] > 0:
                        if name == "dica":
                            self.tip_visible = True
                        self.help_lives[name] -= 1

            # Barrinhas de vida das ajudas
            for i, (name, lives) in enumerate(self.help_lives.items()):
                for j in range(3):
                    bar_x = 730 + i * 110 + j * 10
                    bar_y = 480
                    bar_color = (0, 255, 0) if j < lives else (128, 128, 128)
                    pygame.draw.rect(self.screen, bar_color, (bar_x, bar_y, 8, 15))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
