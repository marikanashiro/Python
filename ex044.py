'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input("Qual é o valor do produto? R$"))
print("""Formas de pagamento:
1 - à vista dinheiro/cheque
2 - à vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão""")
opcao = int(input("Escolha a forma de pagamento (1/2/3/4): "))
if opcao == 1:
    print("O cliente pagará R${:.2f}.".format(valor - (valor * 0.1)))
elif opcao == 2:
    print("O cliente pagará R${:.2f}.".format(valor - (valor * 0.05)))
elif opcao == 3:
    print("O cliente pagará R${:.2f}.".format(valor))
else:
    print("O cliente pagará R${:.2f}.".format(valor + (valor * 0.2)))