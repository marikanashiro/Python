#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da ipotenusa

import math
from math import sqrt
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

h = math.sqrt((ca**2) + (co**2))

print("A hipotenusa do triângulo retângulo é {:.2f}.".format(h))

#OU

h = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}.".format(h))