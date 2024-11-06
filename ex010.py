#Crie um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos dólares ela pode comprar
# considere 1 dolar = 3,27 reais
r = float(input("Quantos reais você tem na carteira? R$ "))
d = r/3.27
print("Com R${:.2f}, você pode comprar US${:.2f}.".format(r, d))