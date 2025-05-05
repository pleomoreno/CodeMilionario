import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            # Se não houver imagem, o botão será apenas o texto
            self.image = self.text
            self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            # Definindo o retângulo da imagem
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        # Centraliza o texto no botão
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def update(self, screen):
        # Exibe a imagem (se houver) e o texto
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        # Verifica se o clique está dentro do retângulo do botão
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        # Altera a cor do texto quando o mouse está sobre o botão
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
