# Nome: Guilherme Penso
# R.A.: 2320311

# Questão 16

valor = int(input("Digite número: "))
operacao = 1
while valor >= 2:
    operacao = operacao * valor
    valor = valor - 1
print(operacao)
print(valor)