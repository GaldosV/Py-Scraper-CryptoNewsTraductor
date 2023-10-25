import os
from ScraperNoticias import scrape_noticia
from ScraperNoticias import obtener_enlaces_noticias
from TraducirNoticias import traducir_texto
from ProcesarYGuardar_BD import procesar_txt_y_guardar_en_db, crear_base_de_datos 

# Enlace principal para las noticias
url_pagina_noticias = 'https://cryptoslate.com/top-news/'

# Llama a la función para crear la base de datos antes de procesar los archivos .txt si no esta creada ya 
crear_base_de_datos()

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

        # Llama a la función para procesar y guardar lso txt  en la base de datos
        procesar_txt_y_guardar_en_db(archivo_txt)

