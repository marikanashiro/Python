'''Faça um programa quqe leia um ano qualquer e mostre se é
bissexto'''

ano = int(input("Digite um ano para saber se ele é bissexto: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é um ano bissexto.".format(ano))
else:
    print("O ano {} não é um ano bissexto.".format(ano))