'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''

peso = float(input("Peso da pessoa: "))
altura = float(input("Altura da pessoa: "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.2f}.".format(imc))
if imc < 18.5:
    print("A pessoa está abaixo do peso.")
elif 18.5 <= imc <= 25:
    print("A pessoa está no seu peso ideal.")
elif imc <= 30:
    print("A pessoa está com sobrepeso.")
elif imc <= 40:
    print("A pessoa está obesa.")
else:
    print("A pessoa está com obesidade mórbida.")
