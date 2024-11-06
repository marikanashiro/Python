'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

num = int(input("Digite um número: "))
print("- 1 para binário")
print("- 2 para octal")
print("- 3 para hexadecimal")
opcao = int(input("Escolha qual será a base de conversão: "))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if opcao == 1:
    print("O número {} convertido para binário é {}.".format(num, binario[2:]))
elif opcao == 2:
    print("O número {} convertido para octal é {}.".format(num, octal[2:]))
elif opcao == 3:
    print("O número {} convertido para hexadecimal é {}.".format(num, hexadecimal[2:]))
else:
    print("ERRO.")