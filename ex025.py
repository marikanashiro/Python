#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input("Digite seu nome completo: ")).strip()
nome_maiusculo = nome.title()
print(nome_maiusculo)
silva = "Silva" in nome_maiusculo

print(silva)