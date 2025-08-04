def cifrado_cesar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            desplazado = (ord(caracter) - base + clave) % 26 + base
            resultado += chr(desplazado)
        else:
            resultado += caracter
    return resultado

def descifrado_cesar(texto, clave):
    return cifrado_cesar(texto, -clave)

def fuerza_bruta(texto_cifrado):
    resultados = []
    for clave in range(1, 26):
        resultado = descifrado_cesar(texto_cifrado, clave)
        resultados.append((clave, resultado))
    return resultados
