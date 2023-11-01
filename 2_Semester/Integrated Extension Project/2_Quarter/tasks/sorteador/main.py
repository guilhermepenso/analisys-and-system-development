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

# usar pandas
#dicionário, usar um loop para separar os nomes com um random de 0 a quantidade de grupos
# colocar dentro de um dataframe como por exemplo:
# df = pd.DataFrame({'store': ['B', 'B', 'A', 'A', 'B', 'B', 'A', 'A'],
                   # 'sales': [12, 25, 8, 14, 10, 20, 30, 30]})

# usar o group by?
# group by store and sort by sales values in descending order
#df.sort_values(['store','sales'],ascending=False).groupby('store').head()

#   store	sales
#1	B	    25
#5	B	    20
#0	B	    12
#4	B	    10
#6	A	    30
#7	A	    30
#3	A	    14
#2	A	    8

# group by store and sort by sales values in ascending order
#df.sort_values(['store','sales']).groupby('store').head()

#	store	sales
#2	A	    8
#3	A	    14
#6	A	    30
#7	A	    30
#4	B	    10
#0	B	    12
#5	B	    20
#1	B	    25

if __name__ == "__main__":
    app.run(debug=True)
