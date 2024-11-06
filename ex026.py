#Faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "a"
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez

frase = str(input("Digite uma frase: ").strip())
min = frase.lower()
qtd = min.count("a")
print("A letra 'a' aparece {} vezes na frase.".format(qtd))
first = min.find("a")
print(first + 1)
last = min.rfind("a")
print(last + 1)