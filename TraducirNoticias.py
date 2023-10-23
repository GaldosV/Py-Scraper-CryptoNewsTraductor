import requests

def traducir_texto(texto_ingles, clave_api):
    # URL de la API de DeepL 
    url = "https://api.deepl.com/v2/translate"

    # Configura los parámetros de la solicitud POST
    params = {
        "auth_key": clave_api,
        "text": texto_ingles,
        "source_lang": "EN",  # Idioma de origen (inglés)
        "target_lang": "ES",  # Idioma de destino (español)
    }

    # Envía la solicitud POST 
    response = requests.post(url, data=params)

    # Analiza la respuesta JSON
    data = response.json()

    # Obtiene el texto traducido
    texto_traducido = data["translations"][0]["text"]

    return texto_traducido


# Pruebas:

# Lee el contenido del archivo de texto
archivo_txt = "Noticias/1.txt"

with open(archivo_txt, "r", encoding="utf-8") as file:
    texto_generado_en_ingles = file.read()

clave_de_api = ""  # Reemplaza con tu clave de API real 

texto_traducido = traducir_texto(texto_generado_en_ingles, clave_de_api)

print("Texto original en inglés:")
print(texto_generado_en_ingles)
print("Texto traducido al español:")
print(texto_traducido)