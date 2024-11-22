Jogo da Forca em Python com Pygame
Este projeto apresenta o clássico jogo da Forca, implementado como parte da disciplina de Algoritmos no curso de Ciências da Computação. O jogo foi desenvolvido utilizando a biblioteca Pygame, com o objetivo de explorar conceitos de programação aplicados ao desenvolvimento de jogos 2D.

📜 Sobre o Projeto
O jogo da Forca consiste em adivinhar uma palavra oculta. O jogador deve tentar descobrir as letras que compõem a palavra antes de esgotar o número máximo de tentativas. A cada erro, uma parte do boneco é desenhada na forca, e o jogo termina quando:

O jogador completa a palavra (vitória).
Todas as partes do boneco são desenhadas (derrota).
Este projeto foi uma oportunidade de aplicar lógica de programação, manipulação gráfica e sonora, bem como reforçar conceitos de estruturação de código e modularidade.

🎮 Funcionalidades
Interface gráfica interativa com uso de imagens e animações.
Sistema de contagem de tentativas com representação visual (boneco da forca).
Escolha aleatória de palavras para cada rodada.
Feedback sonoro para acertos, erros, vitória e derrota.
Design intuitivo e responsivo para diferentes tamanhos de tela.

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem de programação base.
Pygame: Biblioteca para criação e manipulação de elementos visuais e sonoros.

🚀 Como Executar o Projeto
Pré-requisitos
Instale o Python 3.8 ou superior.
Instale a biblioteca Pygame executando:
bash
Copiar código
pip install pygame
Passo a Passo
Clone este repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/jogo-da-forca-pygame.git
Navegue até o diretório do projeto:
bash
Copiar código
cd jogo-da-forca-pygame
Execute o arquivo principal:
bash
Copiar código
python main.py

📷 Imagens do Jogo
Tela Inicial
**img

Durante o Jogo
**img

📚 Como Funciona
Tela Inicial: Clique no botão "Jogar" para iniciar uma nova partida.
Gameplay:
Insira as letras da palavra através do teclado.
Receba feedback visual e sonoro para cada tentativa.
Condições de Encerramento:
Vitória: O jogador adivinha todas as letras corretamente.
Derrota: O desenho do boneco é completado antes de adivinhar a palavra.

📂 Estrutura do Projeto
bash
Copiar código
jogo-da-forca-pygame/
│
├── assets/
│   ├── images/     # Imagens usadas no jogo
│   ├── sounds/     # Arquivos de áudio
│
├── main.py         # Arquivo principal do jogo
├── README.md       # Documentação do projeto

📋 Melhorias Futuras
Adicionar níveis de dificuldade com base na complexidade das palavras.
Permitir seleção de categorias de palavras.
Implementar um modo de dois jogadores.
Melhorar os efeitos sonoros e visuais.

💡 Contribuições
Contribuições são bem-vindas! Caso tenha alguma ideia, sugestão ou correção, sinta-se à vontade para abrir uma issue ou enviar um pull request.

📝 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

🙌 Agradecimentos
Agradecimento especial à comunidade Python e aos desenvolvedores do Pygame.
Ao professor da disciplina de Algoritmos por guiar o desenvolvimento deste projeto.
