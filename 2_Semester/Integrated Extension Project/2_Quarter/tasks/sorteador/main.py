# Importando as bibliotecas necessárias
from flask import Flask, render_template, request  # Flask é um microframework web. render_template é usado para renderizar templates. request é usado para lidar com solicitações HTTP.
import random  # Biblioteca para geração de números aleatórios.

app = Flask(__name__)  # Cria uma nova instância do Flask.

@app.route('/', methods=['GET', 'POST'])  # Define a rota da página inicial. Aceita métodos GET e POST.
def index():  # Define a função que será chamada quando a rota for acessada.
    if request.method == 'POST':  # Se a solicitação for POST, o formulário foi enviado.
        nomes = request.form.get('nomes')  # Obtém os nomes do campo 'nomes' do formulário.
        quantidade_listas = int(request.form.get('quantidade_listas'))  # Obtém a quantidade de listas do campo 'quantidade_listas' do formulário e converte para int.
        nomes = nomes.split(", ")  # Divide a string de nomes em uma lista, usando a vírgula como separador.
        if quantidade_listas > len(nomes):  # Se a quantidade de grupos for maior que a quantidade de nomes, retorna um erro.
            return render_template('index.html', error="A quantidade de grupos não pode ser maior que a quantidade de nomes.")
        random.shuffle(nomes)  # Embaralha a lista de nomes.
        listas = [[] for _ in range(quantidade_listas)]  # Cria uma lista de listas vazias para os grupos.
        for i, nome in enumerate(nomes):  # Para cada nome na lista de nomes.
            listas[i % quantidade_listas].append(nome)  # Adiciona o nome ao grupo correspondente.
        return render_template('index.html', listas=listas)  # Renderiza o template com as listas de grupos.
    return render_template('index.html')  # Se a solicitação for GET, apenas renderiza o template.

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração.
