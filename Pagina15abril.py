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

url = 'https://cnnespanol.cnn.com/2024/04/13/rodolfo-fofo-marquez-juicio-intento-feminicidio-mexico-orix/'


texto_pagina = obtener_texto(url)

if texto_pagina:
    # Convertir el texto a minúsculas y dividirlo en palabras
    palabras = re.findall(r'\b\w+\b', texto_pagina.lower())
    
    conteo_fofo = palabras.count('fofo')
    
    print("La palabra 'fofo' aparece", conteo_fofo, "veces en el texto.")
else:
    print("No se pudo obtener el texto de la página.")
