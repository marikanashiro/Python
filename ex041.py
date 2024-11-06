'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SÊNIOR
- acima: MASTER'''

from datetime import date

ano = int(input("Qual é o ano de nascimento do atleta? "))
anoSistema = date.today().year
idade = anoSistema - ano
if idade <= 9:
    print("Esse atleta é MIRIM!")
elif idade <= 14:
    print("Esse atleta é INFANTIL!")
elif idade <= 19:
    print("Esse atleta é JUNIOR!")
elif idade == 25:
    print("Esse atleta é SÊNIOR!")
else:
    print("Esse atleta é MASTER!")