#Crie um programa que leia o nome completo de uma pessoa e mostre:
#todas as letras maiusculas
#todas as letras minusculas
#quantas letras no total (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip()

maiusculo = nome.upper()
print("Seu nome com todas as letras maiúsculas fica: {}".format(maiusculo))

minusculo = nome.lower()
print("Seu nome com todas as letras minúsculas fica: {}".format(minusculo))

semEspaco = nome.replace(" ", "")
print("Seu nome tem ao todo {} letras.".format(len(semEspaco)))

separado = nome.split()
primeiroNome = separado[0]
print("Seu primeiro nome tem {} letras.".format(len(primeiroNome)))