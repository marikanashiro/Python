#Crie um programa que leia um número real qualquer e mosrte na tela a sua porção inteira
#Ex: o numero 6.127 tem a parte inteira 6
import math
from math import trunc

num = float(input("Digite um número real: "))
pi = math.trunc(num)
print("A porção inteira de {} é {}.".format(num, pi))

#OU (não precisa da linha 7)

#print("O valor digitado foi {} e a sua porção inteira é {}.".format(num, trunc(num)))

#OU sem usar modulos

#print("O valor digitado foi {} e a sua porção inteira é {}.".format(num, int(num)))