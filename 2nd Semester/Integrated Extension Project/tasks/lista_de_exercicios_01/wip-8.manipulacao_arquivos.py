# Nome: Guilherme Penso
# R.A.: 2320311

# 8. Manipulação de Arquivos
# Escreva um programa que leia um arquivo de texto, conte o número de palavras e o número de linhas, e então crie um novo arquivo com essa informação.

with open ("C:\Users\guilh\OneDrive\Documents\Study\Analysis and System Development\2nd Semester\Integrated Extension Project\tasks\lista_de_exercicios_01\text.txt", "r") as arquivo:
    text = arquivo.read()
print (text)
