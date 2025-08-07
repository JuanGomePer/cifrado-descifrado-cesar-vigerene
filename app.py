from flask import Flask, render_template, request
from cesar import cifrado_cesar, descifrado_cesar, fuerza_bruta
from vigenere import vigenere_cifrar, vigenere_descifrar, vigenere_fuerza_bruta, cargar_diccionario


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
            if not clave_raw:
                resultado = "Debes ingresar una clave numérica para cifrar."
            else:
                resultado = cifrado_cesar(texto, clave)
        elif accion == "descifrar" and clave_raw:
            resultado = descifrado_cesar(texto, clave)
        elif accion == "descifrar" and not clave_raw:
            resultados_bruta = fuerza_bruta(texto)

    return render_template("cesar.html", resultado=resultado, resultados_bruta=resultados_bruta)

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    resultado = ""
    resultados_bruta = []

    if request.method == "POST":
        mensaje = request.form.get("mensaje", "").strip()
        clave = request.form.get("clave", "").strip()
        accion = request.form.get("accion")

        if accion == "cifrar":
            if mensaje and clave:
                resultado = vigenere_cifrar(mensaje, clave)
            else:
                resultado = "Debes ingresar un mensaje y una clave."
        
        elif accion == "descifrar":
            if mensaje and clave:
                diccionario = cargar_diccionario("diccionario.txt", 100)
                if clave.upper() not in diccionario:
                    resultado = "No se ha podido descifrar: la clave no está en el diccionario."
                else:
                    resultado = vigenere_descifrar(mensaje, clave)
            elif mensaje and not clave:
                diccionario = cargar_diccionario("diccionario.txt", 100)
                resultados_bruta = vigenere_fuerza_bruta(mensaje, diccionario)
            else:
                resultado = "Debes ingresar un mensaje para descifrar."

    return render_template("vigenere.html", resultado=resultado, resultados_bruta=resultados_bruta)


    resultado = ""
    resultados_bruta = []

    if request.method == "POST":
        mensaje = request.form.get("mensaje")
        clave = request.form.get("clave")
        accion = request.form.get("accion")

        if accion == "cifrar":
            if mensaje and clave:
                resultado = vigenere_cifrar(mensaje, clave)
        elif accion == "descifrar" and clave:
            resultado = vigenere_descifrar(mensaje, clave)
        elif accion == "descifrar" and not clave:
            diccionario = cargar_diccionario("diccionario.txt", 100)
            resultados_bruta = vigenere_fuerza_bruta(mensaje, diccionario)

    return render_template("vigenere.html", resultado=resultado, resultados_bruta=resultados_bruta)

if __name__ == "__main__":
    app.run(debug=True)
