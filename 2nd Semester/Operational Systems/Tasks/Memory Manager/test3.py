while True:
    
    process_name = str (input("Digite o Nome do Processo: "))
    process_size = int (input("Digite o Tamanho do Processo: "))
    block_list= []

    for i in range(process_size):
        block_list.append(process_name)
        
    print(block_list)
    
    choose = input("Deseja alocar mais memória? [S/N]: ")
    
    if (choose == "N") or (choose == "n"):
        break