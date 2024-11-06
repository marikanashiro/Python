#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import cos, sin, tan, radians
angulo = float(input("Digite um ângulo: "))

#primeiro tem que converter o angulo para radianos:

rad = radians(angulo)

#calculando seno, cosseno e tangente:
c = cos(rad)
s = sin(rad)
t = tan(rad)

print("O ângulo {:.2f} tem cosseno {:.2f}, seno {:.2f} e tangente {:.2f}.".format(angulo, c, s, t))