def limpiar_texto(texto):
    return ''.join([c.upper() for c in texto if c.isalpha()])

def vigenere_cifrar(mensaje, clave):
    clave = ''.join([c.upper() for c in clave if c.isalpha()])
    resultado = []
    j = 0  # índice para clave

    for caracter in mensaje:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            m = ord(caracter) - base
            k = ord(clave[j % len(clave)]) - ord('A')
            c = (m + k) % 26
            resultado.append(chr(c + base))
            j += 1
        else:
            resultado.append(caracter)  # conserva espacios y símbolos

    return ''.join(resultado)

def vigenere_descifrar(mensaje_cifrado, clave):
    clave = ''.join([c.upper() for c in clave if c.isalpha()])
    resultado = []
    j = 0

    for caracter in mensaje_cifrado:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            c = ord(caracter) - base
            k = ord(clave[j % len(clave)]) - ord('A')
            m = (c - k + 26) % 26
            resultado.append(chr(m + base))
            j += 1
        else:
            resultado.append(caracter)

    return ''.join(resultado)

def cargar_diccionario(path="diccionario.txt", limite=100):
    try:
        with open(path, encoding='utf-8') as archivo:
            contenido = archivo.read()
            if "passwords" in contenido:
                contexto = {}
                exec(contenido, contexto)
                lista = contexto.get("passwords", [])
                return [clave.upper() for clave in lista if clave.isalpha()][:limite]
            else:
                return []
    except Exception as e:
        print("❌ Error al cargar diccionario:", e)
        return []

def vigenere_fuerza_bruta(mensaje_cifrado, diccionario):
    resultados = []
    for clave in diccionario:
        intento = vigenere_descifrar(mensaje_cifrado, clave)
        resultados.append((clave, intento))
    return resultados
