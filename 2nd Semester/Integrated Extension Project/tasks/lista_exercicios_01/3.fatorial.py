# Nome: Guilherme Penso
# R.A.: 2320311

# 3. Fatorial
# Escreva uma função que calcule o fatorial de um número inteiro informado pelo usuário.

n = int(input("Digite o número a ser fatorado: "))

z = n
x = n

while x > 1:
    x = x - 1
    z = z * x
    print (z)