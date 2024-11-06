#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#EX: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#num = input("Digite um número entre 0 e 9999: ")
#num = num.zfill(4)
#print(f"Unidade: {num[3]}")
#print(f"Dezena: {num[2]}")
#print(f"Centena: {num[1]}")
#print(f"Milhar: {num[0]}")

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o número {}...".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))