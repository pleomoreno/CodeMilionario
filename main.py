import pygame
import button

start = pygame.init()

# create display window
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Milionário")

# load button images
start_img = pygame.image.load("images/botao_iniciar.png").convert_alpha()
exit_img = pygame.image.load("images/botao_sair.png").convert_alpha()
options_img = pygame.image.load("images/botao_opcoes.png").convert_alpha()
background = pygame.image.load("images/background.png").convert()

start_img = pygame.transform.scale(start_img, (225, 90))
exit_img = pygame.transform.scale(exit_img, (225, 90))
options_img = pygame.transform.scale(options_img, (225, 90))

# create button instances
start_button = button.Button(427, 260, start_img)
options_button = button.Button(427, 410, options_img)
exit_button = button.Button(427, 560, exit_img)

# load logo image
logo_img = pygame.image.load("images/logo.png").convert_alpha()

# game loop
run = True
while run:
    screen.blit(background, (0, 0))
    screen.blit(logo_img, ((SCREEN_WIDTH - logo_img.get_width()) // 2, 30))

    clicked_start = start_button.draw(screen)
    clicked_options = options_button.draw(screen)
    clicked_exit = exit_button.draw(screen)

    if clicked_start:
        print("Start button clicked!")
    if clicked_options:
        print("Options button clicked!")
    if clicked_exit:
        print("Exit button clicked!")
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# quit pygame
pygame.quit()