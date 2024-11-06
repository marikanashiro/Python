#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro = Ana
#ultimo = Souza

nome = str(input("Digite um nome completo: ")).strip()
strings = nome.split(" ")
first = strings[0]
print(first)
last = strings[-1]
print(last)