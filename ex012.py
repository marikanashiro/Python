#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço com 5% de desconto
p = float(input("Qual o preço do seu produto? R$"))
d = p - (p * 0.05)
print("Seu produto com desconto de 5% é R${:.2f}.".format(d))