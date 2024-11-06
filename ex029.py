'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
Não tem else'''

velocidade = float(input("Qual a velocidade que o carro estava andando? "))

multa = (velocidade - 80.00) * 7.00

if velocidade > 80.00:
    print("Você levou uma multa de R${:.2f}.".format(multa))
else:
    print("Continue assim, dirija sempre com cuidado!")
