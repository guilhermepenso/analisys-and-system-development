
# import cep
def cep_request():
    import requests
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        info = response.json()
        
        cidade = info["localidade"]
        uf = info["uf"]
    else:
        print(f"A solicitação falhou com o código de status {response.status_code}")

#data / hora
def data_hora(): 
    import datetime

    data_hora_atual = datetime.datetime.now()

    formato = "%Y-%m-%d %H:%M:%S"
    data = data_hora_atual.strftime(formato)


#COMEÇO

data = ("")
cidade = ("")
uf = ("")

peso = float (input("Digite o peso(kg): "))
cpf = input("Digite o seu CPF: ")
cep = input("Digite o CEP: ")

cep_request()
data_hora()

print(uf)
print(cidade)
print(data)
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


# mandar pro arquivo
with open(r"C:\Users\guilh\OneDrive\Documents\Study\Analysis and System Development\2nd Semester\Integrated Extension Project\tasks\trabalho_preco_frete\Historico.txt", "a") as f:
        f.write("CPF: {}\n".format(cpf))
        f.write("Cep: {}\n".format(cep))
        f.write("data: {}\n".format(data))
        f.write("Peso: {}\n".format(peso))
        f.write("UF: {}\n".format(uf))        
        f.write("Cidade: {}\n".format(cidade))
        f.write("Valor: R$ {}\n".format(valor))
        