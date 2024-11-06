'''Crie um programa que faça o computador jogar jokenpo com você'''

import random

jogador = str(input("Escolha pedra, papel ou tesoura: "))
lista = ["pedra", "papel", "tesoura"]
computador = random.choice(lista)
input("O computador escolheu: {}.".format(computador))

if computador == jogador:
    print("EMPATE!")
elif (computador == 'pedra' and jogador == 'tesoura') or (computador == 'tesoura' and jogador == 'papel') or (computador == 'papel' and jogador == 'pedra'):
    print("O computador ganhou... Tente novamente.")
else:
    print("PARABÉNS! Você ganhou.")