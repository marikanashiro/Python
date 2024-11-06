#Escreva um programa que converta uma temperatura digitada em
#°C para °F

c = float(input("Digite sua temperatura em °C: "))
f = (c * 1.8) + 32
print("A temperatura {0}°C convertida para Fahrenheit é {1}°F.".format(c, f))
