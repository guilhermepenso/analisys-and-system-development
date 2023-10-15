# Nome: Guilherme Penso
# R.A.: 2320311

# 2. Lista de Número Pares 
# Escreva um programa que crie uma lista contendo todos os números pares entre 1 e 100.

list = []
for x in range (101):
    if (x % 2) == 0:
        list.append(x)
print(list)