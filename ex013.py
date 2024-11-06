#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento
s = float(input("Digite seu salário: R$"))
p = 0.15 * s
ns = s + p
print("Seu salário com aumento de 15% é R${:.2f}.".format(ns))