from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

titulo = "Copa do Mundo 2026"
selecoes = []

@app.route("/")
def home():
    return render_template("index.html", titulo=titulo, selecoes=selecoes)

@app.route("/add", methods=["POST"])
def add():
    selecao = request.form.get("selecao")
    continente = request.form.get("continente")
    titulos = request.form.get("titulos")

    if selecao and continente and titulos:
        selecoes.append({
            "selecao": selecao.strip(),
            "continente": continente.strip(),
            "titulos": int(titulos.strip())
        })
    return redirect(url_for("home"))

@app.route("/clear")
def clear():
    selecoes.clear()
    return redirect(url_for("home"))

@app.route("/delete/<nome>")
def delete(nome):
    global selecoes
    selecoes = [s for s in selecoes if s["selecao"] != nome]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
