from flask import Flask, redirect, request, render_template
from mysql import connector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        senha = request.form.get("senha")

        dados = (
            nome, telefone, email, senha
        )

        conect = connector.connect(
            host="localhost",
            database="conexao_python",
            user="root",
            password="Vergil1@"
        )

        cursor = conect.cursor()

        query = """
            INSERT INTO cadastro (nome, telefone, email, senha)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, dados)
        conect.commit()
        cursor.close()
        conect.close()

        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)