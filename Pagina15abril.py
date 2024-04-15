import requests
from bs4 import BeautifulSoup
import re

def obtener_texto(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        texto = ' '.join([p.get_text() for p in soup.find_all('p')])
        return texto
    else:
        print("Error al obtener la página:", response.status_code)
        return None

def contar_palabra_en_texto(texto, palabra):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    conteo = palabras.count(palabra.lower())
    return conteo

url = input("Introduce la URL de la página web: ")
palabra_buscar = input("Introduce la palabra que deseas buscar: ")

texto_pagina = obtener_texto(url)

if texto_pagina:
    conteo_palabra = contar_palabra_en_texto(texto_pagina, palabra_buscar)
    print(f"La palabra '{palabra_buscar}' aparece {conteo_palabra} veces en el texto.")
else:
    print("No se pudo obtener el texto de la página.")
