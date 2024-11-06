#Crie um programa que leia o nome de uma cidade e diga se ela começou ou não com o nome "SANTO"

cidade = str(input("Digite o nome de uma cidade: "))

cidade_title = cidade.title().strip()

frase = cidade_title.startswith("Santo")
print(frase)

#OU

#print(cidade[:5].upper() == 'SANTO')