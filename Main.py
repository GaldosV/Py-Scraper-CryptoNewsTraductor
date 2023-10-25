import os
from ScraperNoticias import scrape_noticia
from ScraperNoticias import obtener_enlaces_noticias
from TraducirNoticias import traducir_texto

# Enlace principal para las noticias
url_pagina_noticias = 'https://cryptoslate.com/top-news/'

# Se obtienen los enlaces de las noticias
url = obtener_enlaces_noticias(url_pagina_noticias)

# Directorio de Noticias
directorio_noticias = "Noticias"

#clave Api de deepL
clave_api=''

# Crear una lista para realizar un seguimiento de los nombres de archivo ya traducidos
archivos_traducidos = []

# Verificar si el directorio de Noticias existe, si no, crearlo
if not os.path.exists(directorio_noticias):
    os.makedirs(directorio_noticias)

# Escanea el directorio de Noticias para obtener los archivos .txt ya traducidos y asi reducir el numero de calls a la api 
for archivo in os.listdir(directorio_noticias):
    if archivo.endswith(".txt"):
        archivos_traducidos.append(archivo)

# Scrape de la información de todos los enlaces de las noticias
for enlace in url:
    nombre_archivo = f'noticia_{enlace.replace("https://", "").replace("/", "_")}.txt'
    if nombre_archivo not in archivos_traducidos:
        scrape_noticia(enlace)
        archivo_txt = os.path.join(directorio_noticias, nombre_archivo)
        with open(archivo_txt, "r", encoding="utf-8") as file:
            texto_generado_en_ingles = file.read()
        # Realiza la traducción solo si es un archivo nuevo
        texto_traducido = traducir_texto(texto_generado_en_ingles, clave_api)
        # Agrega el nombre del archivo a la lista de archivos traducidos
        archivos_traducidos.append(nombre_archivo)

#Pruebas 

# prueba individual para comprobar que funciona con 1 noticia 

# Prueba del enlace para  la noticia a scrapear   https://cryptoslate.com/top-news/ https://cryptoslate.com/sec-drops-charges-against-ripple-executives/
# url_noticia = 'https://cryptoslate.com/sec-drops-charges-against-ripple-executives/'
# scrape_noticia(url_noticia)
