import pygame
import sys
import random # Biblioteca que ficara responsável por selecionar uma palavra aleatoriamente dentro
#da variavel de palavras_disponiveis 


# Inicialização do Pygame
pygame.init()
# Inicialização do Comando de Audio
pygame.mixer.init()

# Dimensões da Tela
Altura = 600
Largura = 600

# Inicialização e Criação da Tela
tela = pygame.display.set_mode((Altura, Largura)) # Criação da janela com a altura e largura definidas anteriormente 
pygame.display.set_caption("Jogo da Forca") # Definição do título da janela 

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
amarela_corpo = (249, 187, 75)
amarelo_cabeça = (255, 215, 130)
azul = (135, 206, 233)

# Fonte Tamanho
# Será utilizada para a criação da palavra na Tela
fonte = pygame.font.Font(None, 100)
# Centralizar a palavra na tela



# Escolha da Palavra
palavras_disponiveis = ["PYTHON"] # Nessa lista ficam todas as palavras disponiveis para aparecerem na tela do jogo

 # Coloquei apenas uma palavra na lista para facilitar a apresentação. Mas poderia ser por exemplo: palavras_disponiveis = ["PYTHON", "INSTAGRAM", "ANIMAL", "AMOR", "FAMILIA", "UFMA", "FUTEBOL"] 
 # que a palvra será escolhida aleatoriamente dentro da lista

palavra_selecionada = random.choice(palavras_disponiveis) # Essa variavel escolhe uma palavra aleatória  dentro da lista de palavras disponiveis
# Choice é uma função da Biblioteca random que escolhe um elemento aleatório na lista 
letras_corretas = set() # Conjunto vazio para armazenar todas as letras corretas
# O set esta sendo utilizado para garantir que não terão letras repetidas

# Centralizar a palavra na tela
#largura_palavra = fonte.size(palavra_selecionada)[0]
largura_palavra = len(palavra_selecionada) * 80  # Supondo que cada letra ocupa 50 pixels
pos_x_palavra = (Largura - largura_palavra) // 2

# Chances:
# Essa variavel ficara responsável por controlar o numero de vidas e de acordo com ela o desenho 
# do boneco irá se modificando 
tentativas = 6

# Posição inicial do boneco:
# Variaveis de medidas para auxiliar a criação do desenho na tela, que será feito utilizando ferramentas de desenho do pygame
pos_x, pos_y = Largura // 2, Altura // 2 - 80  # Um pouco acima do centro
# Tamanho e largura do boneco
tamanho_cabeca = 50
largura_linhas = 15

# Criação da Tela de Start
background = pygame.image.load('fundo_start.jpg').convert()# Atribuindo imagem de fundo para a tela de start
botao_start = pygame.image.load('start.png').convert_alpha()# Atribuindo uma imagem ao Botão
# o conver_alpha está sendo utilizado para otimizar a qualidade da imagem
botao_start_rect = botao_start.get_rect(center=(Altura // 2, Largura // 2))# Redimensionamento do Botão
botao_start = pygame.transform.scale(botao_start, (600,600))# Redimensionamento do Botão
botao_start_rect = botao_start.get_rect(center=(300,453))

# Criação do Botão de "Tente Novamente!"
botao_tente_novamente = pygame.image.load('botão_tente_novamente.png').convert_alpha()# Atribuindo uma imagem ao Botão
# o conver_alpha está sendo utilizado para otimizar a qualidade da imagem
botao_tente_novamente = pygame.transform.scale(botao_tente_novamente, (600, 600))# Redimensionamento do Botão
botao_tente_novamente_rect = botao_tente_novamente.get_rect(center=(300, 300))# Redimensionamento do Botão

#Criação do Botão de "Acerto!"
botao_acerto = pygame.image.load('botão_acerto.png').convert_alpha()# Atribuindo uma imagem ao Botão
# o conver_alpha está sendo utilizado para otimizar a qualidade da imagem
botao_acerto = pygame.transform.scale(botao_acerto, (600, 600))# Redimensionamento do Botão
botao_acerto_rect = botao_acerto.get_rect(center=(300, 300))# Redimensionamento do Botão

# Efeitos Sonoros:
audio_acerto = pygame.mixer.Sound("audio_acerto.mp3")   # Atribuindo arquivos 
audio_erro = pygame.mixer.Sound("audio_erro.mp3")
audio_start = pygame.mixer.Sound("som_start.mp3")
audio_vitoria = pygame.mixer.Sound("som_vitoria.mp3")
audio_derrota = pygame.mixer.Sound("audio_derrota.mp3")
audio_fundo = pygame.mixer.Sound("som_de_fundo.mp3")
# Configurando para o som de fundo ficar mais baixo:
audio_fundo.set_volume(0.45) #O volume fica em 45% agora
audio_fundo.play(-1) #O menos 1 faz o aúdio rodar em looping infinito

# Definir variável para verificar se o jogo começou
jogo_iniciado = False # Essa variavel ficara responsavel por controlar o inico do jogo, quando o Botão de Start for acionado
# ela se torna True e o loop da tela de Start é encerrado 


# Loop Tela de Start
while True: # Cria um loop infinito  
    for event in pygame.event.get(): # Analisa os eventos na janela
        if event.type == pygame.QUIT:# Verifica se o botão de fechar a janela foi pressionado
            pygame.quit()# Encerra o PYGAME
            sys.exit() # Encerra o programa

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verifica se o Botão de Start foi clicado
            if botao_start_rect.collidepoint(event.pos):
                jogo_iniciado = True # Se o botão foi clicado, a variavel vira True e o jogo é iniciado
                audio_start.play() # Reprodução do Som de Start ao botão ser clicado 

    # Desenhar a tela de início
    tela.blit(background, (0, 0)) # Coloca a imagem de fundo da Tela de Start
    tela.blit(botao_start, botao_start_rect) # Coloca o botão de start na tela
    pygame.display.flip()

    # Se o jogo foi iniciado, o break é acionado e o loop encerrado, dando inicio a outra tela do jogo
    if jogo_iniciado:
        break

# Laço de repetição do Jogo
while True:# Cria um loop infinito
    for event in pygame.event.get():# Analisa os eventos na janela
        if event.type == pygame.QUIT:# Verifica se o botão de fechar a janela foi pressionado
            pygame.quit()# Encerra o PYGAME
            sys.exit()# Encerra o programa

        elif event.type == pygame.KEYDOWN: # Verifica o clique que foi dado no teclado
            if event.key >= pygame.K_a and event.key <= pygame.K_z: # Verifica se o clique foi em alguma letra(A a Z)
                letra = chr(event.key).upper() # Se o clique foi am alguma Letra, ela assume a Variavel letra
                # Upper manipula a variavel pra que ela se torne letra maiuscula, isso é essencial já que todas ás
                # palavras estarão em letras maiusculas dentro da lista de palavras_disponiveis
                if letra not in letras_corretas: # Esse if verifica se a letra não já foi clicada anteriormente 
                    letras_corretas.add(letra) # Caso nunca tenha sido clicada, ela entra para as letras corretas  
                    if letra in palavra_selecionada: # Verifica se a letra clicada faz parte da palavra selecionada 
                        audio_acerto.play() # Reproduz um som de acerto se a tecla estiver na palavra
                    else:
                        audio_erro.play() # Reproduz um som de erro caso a letra não esteja na palavra e 
                        # o numero de tentativas do player diminui em 1  
                        tentativas -= 1 
        # Verifica os cliques dos botões de tente_novamnete e acerto  
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if tentativas == 0 and botao_tente_novamente_rect.collidepoint(event.pos):
                # Reinicia o jogo
                palavra_selecionada = random.choice(palavras_disponiveis) # Escolhe uma nova palavra 
                letras_corretas = set() # Reinicia as letras selecionadas e corretas
                tentativas = 6 # Reinicia a quantidade de tentativas  

            elif all(letra in letras_corretas for letra in palavra_selecionada) and botao_acerto_rect.collidepoint(event.pos):
                # Verifica se a ás letras estão corretas e se o botão de acerto foi clicado 
                # Reinicia o jogo com uma nova palavra
                palavra_selecionada = random.choice(palavras_disponiveis) # Escolhe uma nova palavra
                letras_corretas = set() # Reinicia as letras selecionadas e corretas
                tentativas = 6 # Reinicia a quantidade de tentativas



    # Desenho da tela principal do jogo
    fundo = pygame.image.load("fundo_do_game.png")  # Atribui o arquivo de imagem para a variavel   
    tela.blit(fundo, (0,0)) # Desenha a imagem na tela  




    # Desenho da Palavra Invisível
    palavra_invisivel = " " # Esta variavel será a que aparecerá na tela 
    for letra in palavra_selecionada: # Para cada letra da palavra_selecionada será atribuido um "_", a medida em que 
        # o player for acertando as letras, o "_" será substituido pela então letra
        if letra in letras_corretas:
            palavra_invisivel += letra + " "
        else:
            palavra_invisivel += " _ "

    palavra_na_tela = fonte.render(palavra_invisivel, True, branco) # Caracteristicas e posição do texto
    tela.blit(palavra_na_tela, (pos_x_palavra, 380)) # Desenha a palavra na tela

    # Desenho do Boneco de Acordo com o número de tentativas, a cada vida perdida o boneco perde um membro do corpo
    # até chegar a 0 e o botão de derrota ser acionado, ou então, se o usuario acertar a palavra antes das tentetivas 
    # chegarem a 0 e o botão de vitória ser acionado dando a opção de reiniciar o jogo
    if tentativas == 6: # Com 6 tentativas restantes o player tera ainda todo o boneco na tela
        perna_esquerda = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + 2*tamanho_cabeca), (pos_x + tamanho_cabeca//2, pos_y + 3*tamanho_cabeca), largura_linhas)
        cabeça = pygame.draw.circle(tela, amarelo_cabeça, (pos_x, pos_y - tamanho_cabeca), tamanho_cabeca)
        corpo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y), (pos_x, pos_y + 2*tamanho_cabeca), largura_linhas)
        braço_direito = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x - tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas)
        braço_esquerdo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x + tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas)
        perna_direita = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + 2*tamanho_cabeca), (pos_x - tamanho_cabeca//2, pos_y + 3*tamanho_cabeca), largura_linhas)
    if tentativas == 5: # Com 5 tentativas restantes o player tera ainda a cabeça, tronco, os dois braços e uma perna do boneco na tela
        cabeça = pygame.draw.circle(tela, amarelo_cabeça, (pos_x, pos_y - tamanho_cabeca), tamanho_cabeca)
        corpo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y), (pos_x, pos_y + 2*tamanho_cabeca), largura_linhas)
        braço_direito = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x - tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas)
        braço_esquerdo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x + tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas)
        perna_direita = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + 2*tamanho_cabeca), (pos_x - tamanho_cabeca//2, pos_y + 3*tamanho_cabeca), largura_linhas)
    if tentativas == 4: # Com 4 tentativas restantes o player tera ainda a cabeça, tronco e os dois braços do boneco na tela
        cabeça = pygame.draw.circle(tela, amarelo_cabeça, (pos_x, pos_y - tamanho_cabeca), tamanho_cabeca)
        corpo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y), (pos_x, pos_y + 2*tamanho_cabeca), largura_linhas)
        braço_direito = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x - tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas)
        braço_esquerdo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x + tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas) 
    if tentativas == 3: # Com 3 tentativas restantes o player tera ainda a cabeça, tronco e um braço do boneco na tela
        cabeça = pygame.draw.circle(tela, amarelo_cabeça, (pos_x, pos_y - tamanho_cabeca), tamanho_cabeca)
        corpo = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y), (pos_x, pos_y + 2*tamanho_cabeca), largura_linhas)
        braço_direito = pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y + tamanho_cabeca//2), (pos_x - tamanho_cabeca, pos_y + tamanho_cabeca), largura_linhas)
    if tentativas == 2: # Com duas tentativas restantes o player tera a cabeça e o corpo do boneco na tela
        pygame.draw.circle(tela, amarelo_cabeça, (pos_x, pos_y - tamanho_cabeca), tamanho_cabeca)
        pygame.draw.line(tela, amarela_corpo, (pos_x, pos_y), (pos_x, pos_y + 2 * tamanho_cabeca), largura_linhas)
    if tentativas == 1: # Com uma tentativa restante o player tera apenas a cabeça do boneco na sua tela
        pygame.draw.circle(tela, amarelo_cabeça, (pos_x, pos_y - tamanho_cabeca), tamanho_cabeca)
    
    # Condiçoes de Vitória ou derrota de acordo com o número de vidas para desenhar os botões 
    if all(letra in letras_corretas for letra in palavra_selecionada):
        tela.blit(botao_acerto, botao_acerto_rect)
        audio_vitoria.play(1) # Efeito sonoro de vitória 

    if tentativas == 0: # Se as tentativas chegarem a 0, o player perde e a tela com o botão de tente_novamente é ativado
        tela.blit(botao_tente_novamente, botao_tente_novamente_rect) 
        audio_derrota.play(1) # Junto com o botão vem o efeito sonoro de derrota 
        
  
    pygame.display.update() # Atualizar tela
