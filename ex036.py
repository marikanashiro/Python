'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
negado.'''

valor = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Em quantos anos deseja pagar? "))
prestacao = valor / (anos * 12)
print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.".format(valor, anos, prestacao))
pagamentoMax = salario * 0.30
if prestacao <= pagamentoMax:
    print("Você pode comprar essa casa!".format(prestacao))
else:
    print("Infelizmente, você não pode comprar essa casa.")
