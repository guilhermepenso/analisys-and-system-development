#Nome: Guilherme Penso / R.A.: 2320311
while True:
    print("--- MENU ---")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    
    escolha = input("Digite a escolha da operação: ")
    
    if escolha not in ("1", "2", "3", "4"):
        print ("Escolha Inválida")
        continue
    
    n1 = float(input("Digite o Primeiro Número: "))
    n2 = float(input("Digite o Segundo Número: "))
    
    if escolha == "1":
        result = n1 + n2
        print(n1, " + ", n2, " = ", result)
    elif escolha == "2":
        result = n1 - n2
        print(n1, " - ", n2, " = ", result)
    elif escolha == "3":
        result = n1 * n2
        print(n1, " * ", n2, " = ", result)
    elif escolha == "4":
        result = n1 / n2
        print(n1, " / ", n2, " = ", result)
    else:
        print("Opção Inválida")
        
    resp = input("Deseja continuar?[S/N]")
    
    if (resp == "n") or (resp == "N"):
        break