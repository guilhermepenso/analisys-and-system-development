# Nome: Guilherme Penso
# R.A.: 2320311

# 8. Manipulação de Arquivos
# Escreva um programa que leia um arquivo de texto, conte o número de palavras e o número de linhas, e então crie um novo arquivo com essa informação.

def contar_palavras(arquivo):
    palavras = 0
    with open(arquivo, "r") as f:
        for linha in f:
            palavras += len(linha.split())
    return palavras
def contar_linhas(arquivo):
    linhas = 0
    with open(arquivo, "r") as f:
        for _ in f:
            linhas += 1
    return linhas
def inicio():
    arquivo = input("Digite o endereço do arquivo de entrada: ")
    criar_arquivo = input("Digite o endereço do arquivo de saída:")
    
    palavras = contar_palavras(arquivo)
    linhas = contar_linhas(arquivo)
    
    with open(criar_arquivo, "w") as f:
        f.write("Número de palavras: {}".format(palavras))
        f.write("Número de linhas: {}".format(linhas))

inicio()