'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos podem formar um triângulo ", end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Esse triângulo não pode existir.")


