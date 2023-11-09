from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nomes = request.form.get('nomes')
        quantidade_listas = int(request.form.get('quantidade_listas'))
        nomes = nomes.split(", ")
        if quantidade_listas > len(nomes):
            return render_template('index.html', error="A quantidade de grupos não pode ser maior que a quantidade de nomes.")
        random.shuffle(nomes)
        listas = [[] for _ in range(quantidade_listas)]
        for i, nome in enumerate(nomes):
            listas[i % quantidade_listas].append(nome)
        return render_template('index.html', listas=listas)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
