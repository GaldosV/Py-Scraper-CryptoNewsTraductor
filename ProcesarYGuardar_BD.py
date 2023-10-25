import sqlite3
#Crea la base de datos de noticias si no existe 
def crear_base_de_datos():
    conn = sqlite3.connect('noticias.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS noticias (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            contenido TEXT,
            fecha TEXT,
            enlace TEXT
        )
    ''')
    conn.commit()
    conn.close()

#Verifica que existe la noticia o no antes de imprimirla en la BD 
def verificar_existencia_noticia(titulo, contenido, fecha, enlace):
    conn = sqlite3.connect('noticias.db')
    cursor = conn.execute('SELECT * FROM noticias WHERE titulo = ? AND contenido = ? AND fecha = ? AND enlace = ?', (titulo, contenido, fecha, enlace))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

#Mete las noticias en la base de datos 
def insertar_noticia(titulo, contenido, fecha, enlace):
    conn = sqlite3.connect('noticias.db')
    conn.execute('INSERT INTO noticias (titulo, contenido, fecha, enlace) VALUES (?, ?, ?, ?)', (titulo, contenido, fecha, enlace))
    conn.commit()
    conn.close()
#Procesa las noticas de .txt para poder insertarlas en la base de datos 
def procesar_txt_y_guardar_en_db(archivo_txt):
    with open(archivo_txt, "r", encoding="utf-8") as file:
        contenido = file.read()
    
    # Extraer título, contenido, fecha y enlace desde el contenido del archivo
    titulo = contenido.split('Título de la noticia: ')[1].split('\n')[0]
    contenido = contenido.split('Contenido de la noticia: ')[1].split('\n')[0]
    fecha = contenido.split('Fecha de la Noticia: ')[1].split('\n')[0]
    enlace = contenido.split('Link de la Noticia: ')[1].split('\n')[0]
    
    #verifica que no estan y las mete en la BD 
    if not verificar_existencia_noticia(titulo, contenido, fecha, enlace):
        insertar_noticia(titulo, contenido, fecha, enlace)
        print(f"Noticia insertada en la base de datos: {titulo}")
    else:
        print(f"Noticia ya existente en la base de datos: {titulo}")

#Pruebas

# Llamado a la función para crear la base de datos
crear_base_de_datos()

# Ejemplo de procesamiento de un archivo .txt
archivo_txt = "Noticias/noticia_cryptoslate.com_inflows-into-digital-assets-rise-340-week-on-week-in-anticipation-of-us-spot-bitcoin-etf-report.txt"
procesar_txt_y_guardar_en_db(archivo_txt)