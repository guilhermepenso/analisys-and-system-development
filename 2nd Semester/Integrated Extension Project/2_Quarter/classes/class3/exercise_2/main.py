from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/cadastro", methods=["POST"])
def cadastro():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    cidade = request.form.get("cidade")
    dic = {}
    dic["nome"] = nome
    dic["telefone"] = telefone
    dic["cidade"] = cidade
    return dic

if __name__ == '__main__':
    app.run(debug=True)


def data_hora(): 
    data_hora_atual = datetime.datetime.now()
    formato = "%d/%m/%Y %H:%M:%S"
    formato1 = "%d-%m-%Y"
    data = data_hora_atual.strftime(formato)
    dia = data_hora_atual.strftime(formato1)
    return (data, dia)