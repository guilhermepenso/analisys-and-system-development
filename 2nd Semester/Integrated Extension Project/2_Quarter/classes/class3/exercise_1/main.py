from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/cadastro", methods=["POST"])
def cadastro():
    palavra = request.form.get("palavra")
    data = datetime.datetime.now()
    formato = "%H:%M:%S"
    data = data.strftime(formato)
    dict = {}
    dict["data_pesquisa"] = data
    dict["palavra"] = palavra
    dict["qtde_letras"] = len(palavra)
    return dict

if __name__ == '__main__':
    app.run(debug=True)