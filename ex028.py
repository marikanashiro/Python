'''Escreva um programa que faça o computador pensar em
um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import shuffle
lista = [0, 1, 2, 3, 4, 5]
shuffle(lista)
escolhido = lista[0]
num = int(input("Chute um número entre 0 e 5: "))
print("O número escolhido pelo computador foi: {}.".format(escolhido))
if num == escolhido:
    print("Parabéns, você acertou!")
else:
    print("Tente novamente...")

#OU

'''from random import randint
computador = randint(0, 5)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei?"))
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no número {}".format(computador, jogador))'''