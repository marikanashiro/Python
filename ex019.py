#um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
#o nome deles e escrevendo o nome do escolhido

#import random

#alunos = input("Digite o nome dos alunos separando com vírgula: ")

#sorteado = random.choice(alunos)

#print("O aluno sorteado foi: {}.".format(sorteado))

import random

a1 = input("Digite o nome do aluno 1: ")
a2 = input("Digite o nome do aluno 2: ")
a3 = input("Digite o nome do aluno 3: ")
a4 = input("Digite o nome do aluno 4: ")

lista = [a1, a2, a3, a4]

sorteado = random.choice(lista)

print("O aluno escolhido foi: {}.".format(sorteado))