'''Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.
Para salários superiores a 1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%'''

salarioInicial = float(input("Digite o seu salário para descobrir seu aumento: R$"))

#if salarioInicial > 1250.00:
    #print("Seu novo salário será: {:.2f}".format(salarioInicial * 1.10))
if salarioInicial <= 1250.00:
    print("Seu novo salário será: R${:.2f}".format(salarioInicial * 1.15))
else:
    print("Seu novo salário será: R${:.2f}".format(salarioInicial * 1.10))
