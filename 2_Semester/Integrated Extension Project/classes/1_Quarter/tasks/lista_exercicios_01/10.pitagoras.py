# Nome: Guilherme Penso
# R.A.: 2320311

# 10. Pitágoras
# Escreva um programa que calcule a hipotenusa de um triângulo retângulo.

import math

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hip = math.sqrt(ca**2 + co**2)

print("O valor da hipotenusa é: ", hip)