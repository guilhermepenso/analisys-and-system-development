# Nome: Guilherme Penso
# R.A.: 2320311

# 7. Circuferência
# Escreva um programa que calcule o comprimento e a área de uma circunferência.

pi = 3.14

while True:
    print("-- MENU --")
    print("1. Área")
    print("2. Diâmetro")
    print("3. Circunferência\n")

    escolha = input("Selecione a opção de cálculo ")

    if escolha not in ("1", "2", "3"):
        print("Opção inválida")
        continue

    r = float(input("Digite o Raio da Circunferência: "))

    if escolha == "1":
        a = (pi * (r**2))
        print("Área da circunferência: ", a)
        
    elif escolha == "2":
        d = (2 * r)
        print("Diâmetro da circunferência: ", d)
    elif escolha == "3":
        c = (2 * pi * r)
        print("Circunferência: ", c)