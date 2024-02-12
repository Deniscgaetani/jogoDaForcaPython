# Import
import random
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou linux
    else:
        _ = system('clear')