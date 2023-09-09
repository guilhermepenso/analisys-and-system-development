from itertools import repeat

def alocar(block_name, block_size):
    list_local=[]
    
    while counter != 0:
    list_local.append([block_name] * block_size)
    return (list_local)

block_name = str (input("Digite o Nome do Processo: "))
block_size = int (input("Digite o Tamanho do Processo: "))

list_global = alocar(block_name, block_size)

print(list_global)