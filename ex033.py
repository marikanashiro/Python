'''Faça um programa que leia 3 numeros e mostre qual
é o maior e qual é o menor'''
#ERRADO:::::::::::::::
'''n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
#lista = [n1, n2, n3]
if n1 > n2 and n3:
    print("O maior número é: {}".format(n1))
if n2 > n1 and n3:
        print("O maior número é: {}".format(n2))
else:
        print("O maior número é: {}".format(n3))
if n1 < n2 and n3:
    print("O menor número é: {}".format(n1))
if n2 < n1 and n3:
        print("O menor número é: {}".format(n2))
else:
        print("O menor número é: {}".format(n3))'''

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi: {}".format(menor))
print("O maior valor digitado foi: {}".format(maior))