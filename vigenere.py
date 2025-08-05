def limpiar_texto(texto):
    return ''.join([c.upper() for c in texto if c.isalpha()])

def vigenere_cifrar(mensaje, clave):
    mensaje = limpiar_texto(mensaje)
    clave = limpiar_texto(clave)
    resultado = []

    for i, letra in enumerate(mensaje):
        m = ord(letra) - ord('A')
        k = ord(clave[i % len(clave)]) - ord('A')
        c = (m + k) % 26
        resultado.append(chr(c + ord('A')))

    return ''.join(resultado)

def vigenere_descifrar(mensaje_cifrado, clave):
    mensaje_cifrado = limpiar_texto(mensaje_cifrado)
    clave = limpiar_texto(clave)
    resultado = []

    for i, letra in enumerate(mensaje_cifrado):
        c = ord(letra) - ord('A')
        k = ord(clave[i % len(clave)]) - ord('A')
        m = (c - k + 26) % 26
        resultado.append(chr(m + ord('A')))

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
