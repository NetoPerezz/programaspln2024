import requests
import nltk
from bs4 import BeautifulSoup

# Función para extraer el texto de una página web
def extraer_texto_pagina(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    texto = soup.get_text()
    return texto

# URL de la página web
url_pagina = "https://www.eluniversal.com.mx/tendencias/novia-de-fofo-marquez-rompe-el-silencio-y-se-disculpa-con-su-victima-lamento-de-corazon-todo-esto/"

# Extraer texto de la página web
texto_pagina = extraer_texto_pagina(url_pagina)

# Guardar el texto extraído en un archivo de texto
if texto_pagina:
    with open("texto_pagina.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_pagina)

# Cargar el texto del archivo
archivo_nombre = "texto_pagina.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Contar el número de palabras
num_palabras = len(texto.split())

# Contar el número de líneas de texto
num_lineas = texto.count('\n') + 1

print("----------------------------------------------------------------------")
print("Número de palabras en la página:", num_palabras)
print("Número de líneas de texto en la página:", num_lineas)

# Mostrar palabras de 3 o 4 caracteres
palabras_3_4_caracteres = [palabra for palabra in texto.split() if len(palabra) in [3, 4]]
print("Palabras de 3 o 4 caracteres:", palabras_3_4_caracteres)

# Contar el número de veces que aparece una palabra específica en el texto
palabra_especifica = "palabra"
num_apariciones_palabra = texto.lower().count(palabra_especifica)
print(f"Número de veces que aparece la palabra '{palabra_especifica}': {num_apariciones_palabra}")

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
nltk.download('stopwords')
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabra_funcional in palabras_funcionales:
    print(palabra_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(40)
