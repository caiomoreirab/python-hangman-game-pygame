# \*\*Jogo da Forca - Implementado com Pygame\*\*

Este projeto implementa o clássico \*\*Jogo da Forca\*\*, utilizando a biblioteca \*\*Pygame\*\* em Python. O objetivo do jogo é adivinhar uma palavra oculta antes que o jogador esgote o número de tentativas e o boneco da forca seja desenhado completamente.

## 🚀 \*\*Funcionalidades\*\*
- Interface gráfica interativa criada com \*\*Pygame\*\*.
- Sons de fundo e efeitos sonoros para acertos, erros, vitórias e derrotas.
- Palavras selecionadas aleatoriamente a partir de uma lista pré-definida.
- Exibição dinâmica do progresso da palavra e do boneco da forca.
- Botões interativos para reiniciar o jogo.

## 🛠️ \*\*Tecnologias Utilizadas\*\*
- \*\*Python\*\* (versão 3.8+)
- \*\*Pygame\*\* (para interface gráfica e sons)
- \*\*Random\*\* (para seleção aleatória de palavras)

## 📂 \*\*Estrutura do Projeto\*\*
\```
.
├── main.py                      # Código principal do jogo
├── fundo_start.jpg              # Imagem de fundo da tela inicial
├── start.png                    # Botão "Start" para iniciar o jogo
├── botão_tente_novamente.png    # Botão "Tente Novamente"
├── botão_acerto.png             # Botão "Acerto" para vitória
├── fundo_do_game.png            # Imagem de fundo da tela principal do jogo
├── audio_acerto.mp3             # Efeito sonoro para acerto
├── audio_erro.mp3               # Efeito sonoro para erro
├── som_start.mp3                # Efeito sonoro da tela inicial
├── som_vitoria.mp3              # Efeito sonoro para vitória
├── audio_derrota.mp3            # Efeito sonoro para derrota
├── som_de_fundo.mp3             # Música de fundo
└── README.md                    # Documentação do projeto
\```

## 🧑‍💻 \*\*Como Executar o Projeto\*\*

### \*\*Pré-requisitos\*\*
1. Certifique-se de ter o Python 3.8+ instalado.
2. Instale o Pygame com o comando:
   \```
   pip install pygame
   \```

### \*\*Execução\*\*
1. Baixe todos os arquivos do projeto e mantenha-os na mesma pasta.
2. Execute o arquivo principal do jogo:
   \```
   python main.py
   \```

## 📋 \*\*Regras do Jogo\*\*
- Uma palavra é selecionada aleatoriamente.
- O jogador tem \*\*6 tentativas\*\* para adivinhar a palavra.
- Para cada tentativa errada, uma parte do boneco da forca será desenhada.
- O jogo termina quando o jogador adivinha todas as letras ou esgota as tentativas.

## ⚙️ \*\*Detalhes Técnicos\*\*
### \*\*Funcionalidades do Código\*\*
- \*\*Seleção de palavras\*\*: Utiliza a função \`random.choice\` para selecionar uma palavra da lista \`palavras_disponiveis\`.
- \*\*Interface gráfica\*\*: Usa métodos do Pygame para desenhar textos, imagens e formas geométricas.
- \*\*Efeitos sonoros\*\*: Inclui sons de acerto, erro, vitória e derrota, utilizando o módulo \`pygame.mixer.Sound\`.
- \*\*Controle de tentativas\*\*: O número de tentativas restantes controla a exibição do boneco e as condições de derrota.

### \*\*Extensões Possíveis\*\*
- Adicionar mais palavras à lista \`palavras_disponiveis\`.
- Criar níveis de dificuldade, variando o número de tentativas ou a complexidade das palavras.
- Implementar um sistema de pontuação.

## 🎮 \*\*Controles do Jogo\*\*
- Use o \*\*teclado\*\* para inserir as letras.
- Clique nos botões interativos com o \*\*mouse\*\* para reiniciar o jogo.

## 📜 \*\*Licença\*\*
Este projeto foi desenvolvido como parte da disciplina de Algoritmos no curso de Ciências da Computação. Sinta-se à vontade para estudar e melhorar o código.

## 🤝 \*\*Contribuição\*\*
Contribuições são bem-vindas! Se encontrar problemas ou tiver sugestões de melhoria, envie um \*\*pull request\*\* ou abra uma \*\*issue\*\*.

---

Desenvolvido com 💻 e 🎮 por Caio Moreira 
