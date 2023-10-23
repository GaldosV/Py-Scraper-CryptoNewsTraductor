from ScraperNoticias import scrape_noticia
from ScraperNoticias import obtener_enlaces_noticias
from Traducir_Noticias import traducir_texto

#Enlace principal para las noticias
url_pagina_noticias = 'https://cryptoslate.com/top-news/'

#Se obtienen los enlaces de las noticias 
url = obtener_enlaces_noticias(url_pagina_noticias)

# Scrape de la información de todos los enlaces de las noticias 
for enlace in url:
    scrape_noticia(enlace)

clave= ''




#Pruebas 

# prueba individual para comprobar que funciona con 1 noticia 

# Prueba del enlace para  la noticia a scrapear   https://cryptoslate.com/top-news/ https://cryptoslate.com/sec-drops-charges-against-ripple-executives/
# url_noticia = 'https://cryptoslate.com/sec-drops-charges-against-ripple-executives/'
# scrape_noticia(url_noticia)
