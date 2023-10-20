import os
import requests
from bs4 import BeautifulSoup



def scrape_noticia(url):
    try:
        # Realiza una solicitud HTTP para obtener la página
        response = requests.get(url)

        # Comprueba si la solicitud fue exitosa
        if response.status_code != 200:
            print(f'No se pudo acceder a la página: {url}')
            return

        # Parsea el contenido de la página web con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrae el título de la noticia (si está disponible)
        title = soup.find('h1', class_='post-title')
        if title:
            title = title.get_text()
        else:
            title = 'Título no encontrado'

        # Encuentra el elemento <div class="post-box clearfix">
        post_box = soup.find('div', class_='post-box clearfix')

        if post_box:
            # Encuentra el elemento <article> dentro de post_box
            article = post_box.find('article')

            if article:
                # Excluye el contenido de no deseado (un disclaimer y la bio del autor)
                for unwanted in article.find_all(['div', 'span'], class_=['post-meta-flex', 'footer-disclaimer']):
                    unwanted.extract()

                # Extrae el contenido del artículo
                article_content = ''
                paragraphs = article.find_all('p')
                for p in paragraphs:
                    article_content += p.get_text() + '\n'

                # Extrae la fecha de la noticia (si está disponible)
                article_Date = soup.find('div', class_='post-date')
                if article_Date:
                    article_Date = article_Date.get_text()
                else:
                    article_Date = 'Fecha no encontrada'

                # Link de la noticia (el mismo que el proporcionado)
                article_Link = url

                # Crea la ruta al archivo de texto en la carpeta "Noticias"
                carpeta_noticias = os.path.join(os.path.dirname(__file__), 'Noticias')
                os.makedirs(carpeta_noticias, exist_ok=True)
                nombre_archivo = os.path.join(carpeta_noticias, f'noticia_{article_Link.replace("https://", "").replace("/", "_")}.txt')

                # Abre el archivo en modo escritura y escribe los datos
                with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write('Título de la noticia: ' + title + '\n')
                    archivo.write('Contenido de la noticia: ' + article_content + '\n')
                    archivo.write('Fecha de la Noticia: ' + article_Date + '\n')
                    archivo.write('Link de la Noticia: ' + article_Link + '\n')

                print('Los datos se han guardado en', nombre_archivo)
            else:
                print('No se pudo encontrar el elemento <article> en la página.')
        else:
            print('No se pudo encontrar el elemento <div class="post-box clearfix"> en la página.')

    except Exception as e:
        print(f'Ocurrió un error: {e}')
        
# Prueba del enlace para  la noticia a scrapear   https://cryptoslate.com/top-news/ https://cryptoslate.com/sec-drops-charges-against-ripple-executives/
url_noticia = 'https://cryptoslate.com/sec-drops-charges-against-ripple-executives/'
scrape_noticia(url_noticia)
