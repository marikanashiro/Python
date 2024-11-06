#Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quanto Km foram percorridos? "))
dia = int(input("Por quantos dias o carro ficou alugado? "))
kms = km * 0.15
dias = dia * 60
print("O carro percorreu {}km em um período de {} dias,"
      "totalizando R${:.2f}.".format(km, dia, (kms + dias)))