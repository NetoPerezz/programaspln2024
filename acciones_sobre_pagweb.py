import requests
import nltk

# Solicitar la URL de la página web al usuario
url_pagina = input("Por favor, introduce la URL de la página web: ")

# Obtener el texto de la página web
respuesta = requests.get(url_pagina)
texto_pagina = respuesta.text

# Guardar el texto extraído en un archivo de texto
if texto_pagina:
    with open("texto_pagina.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_pagina)

# Contar el número de palabras
palabras = texto_pagina.split()
num_palabras = len(palabras)

# Contar el número de líneas de texto
lineas = texto_pagina.split("\n")
num_lineas = len(lineas)

# Mostrar palabras de 3 o 4 caracteres
palabras_3_4 = [palabra for palabra in palabras if len(palabra) in (3, 4)]
print("Palabras de 3 o 4 caracteres:", palabras_3_4)

# Contar el número de veces que aparece una palabra fija en el texto
palabra_fija = input("Por favor, introduce la palabra que deseas contar en el texto: ")
apariciones_palabra_fija = palabras.count(palabra_fija)
print(f"Número de veces que aparece '{palabra_fija}' en el texto:", apariciones_palabra_fija)

# Imprimir resultados
print("Número de palabras en la página:", num_palabras)
print("Número de líneas de texto en la página:", num_lineas)

# Cargar palabras funcionales en español de NLTK
nltk.download("stopwords")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto_pagina, language="spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(40)
