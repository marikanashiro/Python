#Faça um programa que leia a largura e a altura de uma
#parede em metros, calcule a sua área e a quantdade de
#tinta necessária para pintá-la, sabendo que cada litro
#de tinta, pinta uma área de 2 metros quadrados
l = float(input("Qual é a largura da parede? "))
a = float(input("Qual é a altura da parede? "))
area = l * a
print("A área da sua parede é de {} m².".format(area))
t = area / 2
print("A quantidade de litros de tinta que você vai precisar é: {} litros.".format(t))