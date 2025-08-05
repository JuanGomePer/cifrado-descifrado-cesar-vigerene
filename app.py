from flask import Flask, render_template, request
from cesar import cifrado_cesar, descifrado_cesar, fuerza_bruta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cesar", methods=["GET", "POST"])
def cesar():
    resultado = ""
    resultados_bruta = []

    if request.method == "POST":
        texto = request.form.get("mensaje")
        clave_raw = request.form.get("clave")
        accion = request.form.get("accion")

        if clave_raw:
            try:
                clave = int(clave_raw)
            except ValueError:
                resultado = "La clave debe ser un número."
                return render_template("cesar.html", resultado=resultado)

        if accion == "cifrar":
            resultado = cifrado_cesar(texto, clave)
        elif accion == "descifrar" and clave_raw:
            resultado = descifrado_cesar(texto, clave)
        elif accion == "descifrar" and not clave_raw:
            resultados_bruta = fuerza_bruta(texto)

    return render_template("cesar.html", resultado=resultado, resultados_bruta=resultados_bruta)

@app.route("/vigerene")
def vigerene():
    return render_template("vigerene.html")

if __name__ == "__main__":
    app.run(debug=True)
