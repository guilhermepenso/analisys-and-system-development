from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/sorteio", methods=["POST"])
def sorteio():
    # Obter os nomes dos participantes
    nomes = request.form.get("nomes")
    num_grupos = request.form.get("num_grupos")
    print(num_grupos)
    
    # Gerar os grupos
    nomes = nomes.split(", ")
    
    grupos = gerar_grupos(nomes, num_grupos)
    
    # Exibir os grupos
    return grupos

def gerar_grupos(nomes, n):
    grupos = [nomes[i::n] for i in range(n)]
    return grupos
    

if __name__ == "__main__":
    app.run(debug=True)
