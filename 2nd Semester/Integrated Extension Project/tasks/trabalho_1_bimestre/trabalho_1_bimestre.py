import requests
import datetime

# Função de Localização de CEP (Retorna o uf(lista_dados[0]) e cidade(lista_dados[1])
def cep_request(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        cidade = info["localidade"]
        uf = info["uf"] 
        return (uf, cidade)
    else:
        print(f"CEP Inválido")

# Função de Data e Hora (Retorna a data atual)
def data_hora(): 
    data_hora_atual = datetime.datetime.now()
    formato = "%d/%m/%Y %H:%M:%S"
    data = data_hora_atual.strftime(formato)
    return (data)

# Função de Valor por Tabela de Preço com verificação de localidade (Retorna Valor)
def tabela_frete(uf, peso):
    if (peso <= 1) and (uf == "SP"):
        valor = 10.00
        print ("Valor do Frete: R$", valor)
    elif (peso <= 1) and (uf != "SP"):
        valor = 12.50
        print ("Valor do Frete: R$", valor)     
    if ((peso >= 1.1) and (peso <= 5.0)) and (uf == "SP"):
        valor = 15.00
        print ("Valor do Frete: R$", valor)
    elif ((peso >= 1.1) and (peso <= 5.0)) and (uf != "SP"):
        valor = 19.90
        print ("Valor do Frete: R$", valor)
    if ((peso >= 5.1) and (peso <= 10.0)) and (uf == "SP"):
        valor = 22.50
        print ("Valor do Frete: R$", valor)
    elif ((peso >= 5.1) and (peso <= 10)) and (uf != "SP"):
        valor = 29.90
        print ("Valor do Frete: R$", valor)
    if (peso > 10.0) and (uf == "SP"):
        valor = 37.50
        print ("Valor do Frete: R$", valor)
    elif (peso > 10.0) and (uf != "SP"):
        valor = 49.90
        print ("Valor do Frete: R$", valor)   
    return (valor)
 
 # Função de criar e escrever os dados em um arquivo .txt   
def arquivo(cpf, cep, peso, uf, cidade, valor, data):
    with open(r"C:\Users\guilh\OneDrive\Documents\Study\Analysis and System Development\2nd Semester\Integrated Extension Project\tasks\trabalho_1_bimestre\historico\historico.txt", "a", encoding="utf-8") as f:
        f.write("CPF: {} | ".format(cpf))
        f.write("Peso: {} Kg | ".format(peso))
        f.write("Valor: R$ {} | ".format(valor))
        f.write("CEP: {} | ".format(cep))
        f.write("UF: {} | ".format(uf))        
        f.write("Cidade: {} | ".format(cidade))
        f.write("Data: {}\n".format(data))
   
# Função de input para os dados base e chamada das outras funções         
def inicio():
    peso = float (input("Digite o peso(Kg): "))
    cpf = input("Digite o seu CPF: ")
    cep = input("Digite o CEP: ")
    lista_dados = cep_request(cep)
    data = data_hora()
    valor = tabela_frete(lista_dados[0], peso)
    arquivo(cpf, cep, peso, lista_dados[0], lista_dados[1], valor, data)

inicio()