# Nome: Guilherme Penso
# R.A.: 2320311

# 9. Conversor de Moeda
# Escreva um programa que converta valores entre diferentes moedas (por exemplo, dólares para euros, euros para libras, etc.)

while True:
    print ("-- CONVERSOR DE MOEDAS--")
    print ("[1] Libras")
    print ("[2] Euro")
    print ("[3] Dólar")
    escolha_moeda1 = input("Escolha a moeda inicial: ")
    escolha_moeda2 = input("Escolha a moeda para converter: ")

    if escolha_moeda1 or escolha_moeda2 not in ('1', '2', '3'):
        print ("Opção Inválida")
        continue

    valor_moeda1 = float(input("Digite o valor: "))

    if (escolha_moeda1 == '1') and (escolha_moeda2 == '2'):
        valor_moeda2 = valor_moeda1 * 1.17
        print ("£", valor_moeda1, "-> €", valor_moeda2)
    elif (escolha_moeda1 == '1') and (escolha_moeda2 == '3'):
        valor_moeda2 = (valor_moeda1 * 1.26)
        print ("£", valor_moeda1, "-> $", valor_moeda2)

    elif (escolha_moeda1 == '2') and (escolha_moeda2 == '1'):
        valor_moeda2 = valor_moeda1 * 0.85
        print ("€", valor_moeda1, "-> £", valor_moeda2)
    elif (escolha_moeda1 == '2') and (escolha_moeda2 == '3'):
        valor_moeda2 = valor_moeda1 * 1.07
        print ("€", valor_moeda1, "-> $", valor_moeda2)
        
    elif (escolha_moeda1 == '3') and (escolha_moeda2 == '1'):
        valor_moeda2 = valor_moeda1 * 0.80
        print ("$", valor_moeda1, "-> £", valor_moeda2)
    elif (escolha_moeda1 == '3') and (escolha_moeda2 == '2'):
        valor_moeda2 = valor_moeda1 * 0.93
        print ("$", valor_moeda1, "-> €", valor_moeda2)

    escolha_saida = input("Deseja fazer outra conversão? [S/N]: ")

    if (escolha_saida == "N") or (escolha_saida == "n"):
        break
