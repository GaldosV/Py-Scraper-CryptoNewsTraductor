import os
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
        title = soup.find('h1', class_='post-title').get_text()

        #Encontrar el articulo y extraer el contenido
         
        # Encuentra el elemento <div class="post-box clearfix">
        post_box = soup.find('div', class_='post-box clearfix')
        # Encuentra el elemento <article> dentro de post_box
        article = post_box.find('article')
        # Extrae el contenido del artículo
        article_content = ''
        paragraphs = article.find_all('p')
        for p in paragraphs:
         article_content += p.get_text() + '\n'

        # Extrae la fecha de la noticia 
        article_Date = soup.find('div', class_='post-date').get_text()

        # Link de la noticia (el mismo que el proporcionado)
        article_Link = url
        
        # Crea la ruta al archivo de texto en la carpeta "Noticias" y llama al archivo noticias + la url 
        nombre_archivo = os.path.join(os.path.dirname(__file__), 'Noticias', f'noticia_{article_Link.replace("https://", "").replace("/", "_")}.txt')


        # Abre el archivo en modo escritura y escribe los datos
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write('Título de la noticia: ' + title + '\n')
            archivo.write('Contenido de la noticia: ' + article_content + '\n')
            archivo.write('Fecha de la Noticia: ' + article_Date + '\n')
            archivo.write('Link de la Noticia: ' + article_Link + '\n')

        print('Los datos se han guardado en', nombre_archivo)
    else:
        print('No a podido encontrar la pagina web ')

# Prueba del enlace para  la noticia a scrapear   https://cryptoslate.com/top-news/ https://cryptoslate.com/sec-drops-charges-against-ripple-executives/
url_noticia = 'https://cryptoslate.com/sec-drops-charges-against-ripple-executives/'
scrape_noticia(url_noticia)
