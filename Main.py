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

        # Imprime la información en el formato deseado
        print('Título de la noticia:', title)
        print('Contenido de la noticia:', article_content)
        print('Fecha de la Noticia:', article_Date)
        print('Link de la Noticia:', article_Link)

    else:
        print('La solicitud no fue exitosa.Algo a fallado')

# Prueba delenlace para  la noticia a scrapear
url_noticia = 'https://www.ejemplo.com/noticia'
scrape_noticia(url_noticia)
