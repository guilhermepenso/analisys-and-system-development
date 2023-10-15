list01 = []

list02 = [1, 2, 3, "Maria", "João", 3.33, [1, 2, 3, "Pedro", [9, [8]]], "maejioahfasnkfnasornwq", "João", "João"]
print (list02)
# dado específico da lista pega com -> []
print (list02[4])
# dado específico da lista dentro da lista -> [][][][][][][][][][][]...
print (list02[6][4][1])
# alterar dado específico da lista -> [] = "..."
list02[3] = "Ana"
print (list02[3])
# adicionar dado na lista -> .append(...)
list02.append(400)
print (list02[8])
list02.append("Ana")
print (list02)
# remove todos os dados da lista
list02.remove("Ana")
print (list02[3])

# apaga posição específica
del list02[0] 

print (list02)

# conta a mesma variável dentro da lista
list02.count("João")

list01.append(input("Digite o número"))
print (list01)

