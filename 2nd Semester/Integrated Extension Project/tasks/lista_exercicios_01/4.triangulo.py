# Nome: Guilherme Penso
# R.A.: 2320311

# 4. Triângulo
# Escreva um programa que leia 3 medidas e informe se as mesmas formam um triângulo.

n1 = input("Digite o tamanho do 1° lado: ")
n2 = input("Digite o tamanho do 2° lado: ")
n3 = input("Digite o tamanho do 3° lado: ")

if n1 == n2 == n3:
    print("É um Triângulo Equilátero")
elif (n1 == n2) or (n1 == n3) or (n2 == n3):
    print("É um Triângulo Isósceles")
else:
    print("É um Triângulo Acutângulo")