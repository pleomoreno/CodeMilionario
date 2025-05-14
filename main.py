import pygame
import button

# Inicializar o Pygame e o mixer
pygame.init()
pygame.mixer.init()

# Criar a janela do jogo
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Milionário")

# Carregar imagens de botões
start_img = pygame.image.load("images/botao_iniciar.png").convert_alpha()
exit_img = pygame.image.load("images/botao_sair.png").convert_alpha()
options_img = pygame.image.load("images/botao_opcoes.png").convert_alpha()
background = pygame.image.load("images/background.png").convert()
music_img = pygame.image.load("images/botao_musica.png").convert_alpha()
sound_img = pygame.image.load("images/botao_som.png").convert_alpha()
back_img = pygame.image.load("images/botao_sair.png").convert_alpha()
fullscreen_img = pygame.image.load("images/botao_tela.png").convert_alpha()

start_img = pygame.transform.scale(start_img, (225, 90))
exit_img = pygame.transform.scale(exit_img, (225, 90))
options_img = pygame.transform.scale(options_img, (225, 90))
music_img = pygame.transform.scale(music_img, (225, 90))
sound_img = pygame.transform.scale(sound_img, (225, 90))
back_img = pygame.transform.scale(back_img, (225, 90))
fullscreen_img = pygame.transform.scale(fullscreen_img, (225, 90))

# Criar instâncias dos botões
start_button = button.Button(427, 260, start_img)
options_button = button.Button(427, 410, options_img)
exit_button = button.Button(427, 560, exit_img)
music_button = button.Button(427, 230, music_img)
sound_button = button.Button(427, 380, sound_img)
back_button = button.Button(30, 600, back_img)
fullscreen_button = button.Button(427, 530, fullscreen_img)

# Carregar imagem do logo
logo_img = pygame.image.load("images/logo.png").convert_alpha()

# Carregar música de fundo
pygame.mixer.music.load('assets/mainmenu.mp3')
pygame.mixer.music.play(-1)  # Tocar em loop
pygame.mixer.music.set_volume(0.5)

# Carregar som do clique
click_sound = pygame.mixer.Sound('assets/button.mp3')

# Carregar imagens para as checkboxes de som
checkbox_on = pygame.image.load("images/checkbox_on.png").convert_alpha()  # Checkbox selecionada
checkbox_off = pygame.image.load("images/checkbox_off.png").convert_alpha()  # Checkbox desmarcada
checkbox_on = pygame.transform.scale(checkbox_on, (60, 60))
checkbox_off = pygame.transform.scale(checkbox_off, (60, 60))

# Carregar a fonte personalizada (substitua pelo caminho correto da sua fonte)
font_path = "assets/Font.ttf"
font_size = 74
font = pygame.font.Font(font_path, font_size)
volume_font_size = 48  # Tamanho menor para o texto do volume
volume_font = pygame.font.Font(font_path, volume_font_size)

# Variáveis de controle
in_options_menu = False  # Flag para verificar se estamos na tela de opções
volume = 0.5  # Volume inicial (50%)
music_playing = True  # A música começa tocando
sound_on = True  # O som está ativado por padrão
is_fullscreen = False

# Função para alternar a música
def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.stop()  # Parar a música
        music_playing = False
    else:
        pygame.mixer.music.play(-1)  # Tocar música em loop
        pygame.mixer.music.set_volume(volume)  # Restaura o volume
        music_playing = True

# Função para alternar o som
def toggle_sound():
    global sound_on
    if sound_on:
        click_sound.set_volume(0)  # Silencia o som
        sound_on = False
    else:
        click_sound.set_volume(1)  # Ativa o som
        sound_on = True

def toggle_fullscreen():
    global is_fullscreen, screen
    if is_fullscreen:
        # Mudar para o modo janela
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        is_fullscreen = False
    else:
        # Mudar para fullscreen
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        is_fullscreen = True

# Função para a tela de ajustes
def show_options_menu():
    global volume
    options_running = True
    while options_running:
        screen.blit(background, (0, 0))

        # Texto de opções
        text = font.render("Opções", True, (0, 227, 197))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 50))

        # Checkboxes para controlar a música
        if music_playing:
            screen.blit(checkbox_on, (680, 245))  # Caixa com som
        else:
            screen.blit(checkbox_off, (680, 245))  # Caixa sem som

        # Checkboxes para controlar o som
        if sound_on:
            screen.blit(checkbox_on, (680, 395))  # Caixa com som
        else:
            screen.blit(checkbox_off, (680, 395))  # Caixa sem som

        # Verificar fullscreen
        if is_fullscreen:
            screen.blit(checkbox_on, (680, 545))  # Caixa de fullscreen ativado
        else:
            screen.blit(checkbox_off, (680, 545))  # Caixa de fullscreen desativado

        # Desenhar os botões
        music_button.draw(screen)  # Botão de música
        sound_button.draw(screen)  # Botão de som
        back_button.draw(screen)   # Botão de voltar
        fullscreen_button.draw(screen)  # Botão de fullscreen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                options_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Verificar qual botão foi clicado:
                if music_button.rect.collidepoint(mouse_pos):  # Clique no botão de música
                    click_sound.play()
                    toggle_music()

                elif sound_button.rect.collidepoint(mouse_pos):  # Clique no botão de som
                    click_sound.play()
                    toggle_sound()
                
                elif fullscreen_button.rect.collidepoint(mouse_pos):  # Clique no botão de fullscreen
                    click_sound.play()
                    toggle_fullscreen()

                elif back_button.rect.collidepoint(mouse_pos):  # Clique no botão de voltar
                    click_sound.play()
                    options_running = False  # Fechar a tela de opções

                elif SCREEN_WIDTH // 2 - 200 < event.pos[0] < SCREEN_WIDTH // 2 + 200 and 300 < event.pos[1] < 320:
                    volume = (event.pos[0] - (SCREEN_WIDTH // 2 - 200)) / 400
                    pygame.mixer.music.set_volume(volume)

        pygame.display.update()

# Loop principal
run = True
while run:
    screen.blit(background, (0, 0))
    screen.blit(logo_img, ((SCREEN_WIDTH - logo_img.get_width()) // 2, 30))

    clicked_start = start_button.draw(screen)
    clicked_options = options_button.draw(screen)
    clicked_exit = exit_button.draw(screen)

    if clicked_start:
        click_sound.play()
        print("Start button clicked!")
    if clicked_options:
        click_sound.play()
        print("Options button clicked!")
        in_options_menu = True  # Ativa a tela de opções
    if clicked_exit:
        click_sound.play()
        print("Exit button clicked!")
        run = False

    if in_options_menu:
        show_options_menu()  # Exibe a tela de opções
        in_options_menu = False  # Após voltar da tela de opções, voltar ao menu principal

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# Fechar o Pygame
pygame.quit()
