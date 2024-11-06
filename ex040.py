'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO'''

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print("A média de notas desse aluno é {:.2f}.".format(media))
if media < 5.0:
    print("O aluno está reprovado.")
elif 5.0 <= media <= 6.9:
    print("O aluno está de recuperação.")
else:
    print("O aluno foi aprovado!")
