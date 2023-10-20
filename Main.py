import requests
from bs4 import BeautifulSoup


def scrape_noticia(url):
    # Realiza una solicitud HTTP para obtener la página
    response = requests.get(url)

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsea el contenido de la página web con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrae el título de la noticia
        title = soup.find('h1').get_text()

        # Extrae el contenido del artículo (tengo que refinarlo un poco mas por que recoge cosas que no son utiles )
        article_content = ''
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            article_content += p.get_text() + '\n'

        # Extrae la fecha de la noticia (tengo que encontrar la id de la fecha asi que por ahora e puesto un placeholder)
        article_Date = soup.find('span', class_='fecha').get_text()

        # Link de la noticia (el mismo que el proporcionado)
        article_Link = url

        # Crea el nombre del archivo basado en el enlace de la noticia para luego hacer busquedas en la BD 
        nombre_archivo = 'noticia_' + article_Link.replace('https://', '').replace('/', '_') + '.txt'

        # Abre el archivo en modo escritura y escribe los datos
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write('Título de la noticia: ' + title + '\n')
            archivo.write('Contenido de la noticia: ' + article_content + '\n')
            archivo.write('Fecha de la Noticia: ' + article_Date + '\n')
            archivo.write('Link de la Noticia: ' + article_Link + '\n')

        print('Los datos se han guardado en', nombre_archivo)
    else:
        print('La solicitud no fue exitosa.Algo a fallado')

# Prueba delenlace para  la noticia a scrapear  
url_noticia = 'https://www.ejemplo.com/noticia'
scrape_noticia(url_noticia)
