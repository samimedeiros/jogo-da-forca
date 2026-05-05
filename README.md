# jogo-da-forca
O jogo da forca consiste adivinhar uma palavra escondida através da indicação das suas letras, uma de cada vez.

1. Objetivo do jogo:

O objetivo do jogo da forca é adivinhar uma palavra secreta, através de vogais e consoantes, antes que o número máximo de tentativas permitidas se esgotem.

2. Regras principais:

a) O jogador tenta adivinhar a palavra colocando uma letra de cada vez.
b) Se a letra pertencer a palavra, ela é revelada nas posições corretas.
c) Se a letra não pertencer, o jogador perde uma tentativa.
d) Letras usadas não podem ser repetidas.
e) O estado atual da palavra é mostrado ao jogador (ex: _ E _ A).

3. Condições de vitória e derrota:

Vitória: O jogador vence se descobrir todas as letras da palavra antes de completar a forca.
Derrota: O jogador perde se completar a forca sem advinhar a palavra.

4. Limitações do sistema:

a) Número de tentativas: 6 a 10 tentativas erradas.
b) Tipo de input: Apenas letras (A-Z), sem números ou caracteres especiais.
c) Validação de input: O sistema deve rejeitar entradas inválidas (ex: mais de uma letra ou símbolos).

5. Requisitos Funcionais 

a) Selecionar palavra aleatória: escolher aleatoriamente uma palavra.
b) Receber input do utilizador: permitir ao jogador introduzir uma letra por tentativa.
c) Validar o input: verificar se o input é uma letra válida (A-Z).
d) Atualizar estado da palavra: mostrar a palavra com as letras corretas e esconder as restantes.
e) Gerir tentativas: mostrar o número de tentativas conforme o jogador erra uma letra.
f) Determinar fim de jogo: verificar se o jogador venceu (palavra completa) ou perdeu (tentativas erradas).

6. Requisitos Não Funcionais (3)

a) Desempenho: O jogo tem que responder às ações do utilizador de forma imediata.
b) Usabilidade: A interface deve ser simples, clara e fácil de entender.
c) Manutenção: O código tem que ser organizado e fácil de perceber, para que possa fazer alterações no futuro, como adicionar novas palavras ou mudar regras do jogo.