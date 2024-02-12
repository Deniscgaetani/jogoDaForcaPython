# Pseudocódigo Jogo da Forca em Python

Aqui está o pseudocódigo detalhado para o jogo da forca:

1. Inicialize uma lista de palavras para o jogo
2. Escolha uma palavra aleatória da lista e armazene em 'palavra_secreta'
3. Crie uma lista 'palavra_mostrada' de espaços vazios do mesmo tamanho da 'palavra_secreta'
4. Defina 'tentativas' como o número de chances que o jogador tem para adivinhar a palavra
5. Enquanto 'tentativas' for maior que zero e 'palavra_mostrada' contiver espaços vazios:
    6. Mostre ao jogador a 'palavra_mostrada'
    7. Mostre ao jogador o número de 'tentativas' restantes
    8. Peça ao jogador para adivinhar uma letra e armazene em 'letra'
    9. Se 'letra' estiver na 'palavra_secreta':
        10. Percorra cada letra em 'palavra_secreta':
            11. Se a letra da 'palavra_secreta' for igual a 'letra':
                12. Atualize a 'palavra_mostrada' com 'letra' na posição correspondente
