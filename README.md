Jogo da Forca - Documentação do Projeto
# Jogo da Forca - Documentação do Projeto
## Descrição do Projeto
O projeto desenvolvido por Caio Moreira é uma implementação do clássico jogo da forca utilizando
a biblioteca Pygame em Python, realizado no contexto da disciplina de Algoritmos no curso de
Ciências da Computação. O jogo consiste em adivinhar uma palavra oculta, onde o jogador tenta
descobrir as letras que a compõem antes de esgotar o número máximo de tentativas.
## Funcionalidades
- O jogador deve tentar adivinhar uma palavra secreta, escolhida aleatoriamente, ao inserir letras
uma de cada vez.
- O número de tentativas é limitado, sendo que a cada erro uma parte do corpo do boneco da forca
é desenhada na tela.
- O jogo termina quando o jogador adivinha a palavra ou esgota suas tentativas, sendo exibida uma
mensagem de vitória ou derrota.
- É possível jogar novamente após o término da partida, reiniciando o jogo com uma nova palavra
secreta.
## Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para o desenvolvimento do jogo.
- **Pygame**: Biblioteca utilizada para a criação da interface gráfica e a lógica do jogo.
- **Algoritmos**: O jogo aplica conceitos de algoritmos para verificar as tentativas dos jogadores e
exibir o estado atual do jogo.
## Como Rodar o Projeto
### Requisitos
Para rodar o jogo em sua máquina, é necessário ter o Python e a biblioteca Pygame instalados.
### Passos para execução:
1. Instale o Python em sua máquina (caso ainda não tenha). Você pode baixá-lo em
https://www.python.org/downloads/.
2. Instale a biblioteca Pygame utilizando o seguinte comando:
 ```bash
 pip install pygame
 ```
3. Clone o repositório ou baixe os arquivos do projeto em seu computador.
4. Abra o terminal ou prompt de comando e navegue até o diretório onde os arquivos do projeto
estão localizados.
5. Execute o jogo utilizando o comando:
 ```bash
 python jogo_da_forca.py
 ```
6. Siga as instruções na tela para jogar.
## Estrutura de Arquivos
- **jogo_da_forca.py**: Arquivo principal do jogo, contendo a implementação da lógica e interface
gráfica.
- **imagens/**: Pasta que contém os recursos visuais utilizados no jogo, como imagens da forca e o
fundo da tela.
## Conclusão
Este projeto visa aplicar conceitos de programação, algoritmos e desenvolvimento de jogos simples
utilizando Pygame. Ele serve como uma base para expandir com novas funcionalidades, como a
implementação de diferentes níveis de dificuldade, pontuação e integração com banco de dados
para salvar os melhores resultados.
Para mais informações ou contribuições, sinta-se à vontade para explorar o código e abrir *issues*
ou *pull requests* no repositório do GitHub.
