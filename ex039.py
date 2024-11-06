'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- se ele ainda vai se alistar no exercito
- se é a hora de se alistar
- se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

pegar o ano do sistema'''

from datetime import date
ano = int(input("Digite o ano de nascimento: "))
anoSistema = date.today().year
idade = anoSistema - ano
if idade < 18:
    print("Ainda não chegou a sua hora, daqui {} ano(s), você terá que se alistar.".format(18 - idade))
elif idade == 18:
    print("Chegou o seu momento! Vá se alistar.")
else:
    print("Seu alistamento está atrasado em {} ano(s), vá se alistar!".format(idade - 18))
