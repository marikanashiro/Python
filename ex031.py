'''Desenvolva um programa que pergunte a distancia
de uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 por km para viagens de até 200km e R$0,45 para viagens
mais longas'''
from operator import ifloordiv

dist = float(input("Qual a distância da sua viagem (em Km): "))

perto = dist * 0.50
longe = dist * 0.45

if dist <= 200.00:
    print("O valor da sua passagem será R${:.2f}.".format(perto))
else:
    print("O valor da sua passagem será R${:.2f}.".format(longe))

#ou
'''if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print("O preço da sua viagem será: {}".format(preco))'''

#ou
#preço = dist * 0.50 if dist <= 200 else dist * 0.45