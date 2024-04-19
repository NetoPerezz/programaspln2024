import docx
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

# Función para contar palabras y líneas
def contar_palabras_y_lineas(texto):
    num_palabras = len(texto.split())
    num_lineas = texto.count('\n') + 1
    return num_palabras, num_lineas

# Función para contar la frecuencia de una palabra específica
def contar_apariciones(texto, palabra):
    return texto.lower().count(palabra.lower())

# Leer el documento de Word
documento = docx.Document("word.docx")
texto_documento = ""
for parrafo in documento.paragraphs:
    texto_documento += parrafo.text + "\n"

# Contar palabras y líneas
num_palabras, num_lineas = contar_palabras_y_lineas(texto_documento)
print("Número de palabras en el documento:", num_palabras)
print("Número de líneas de texto en el documento:", num_lineas)

# Contar apariciones de una palabra específica
palabra_a_contar = "palabra"
num_apariciones = contar_apariciones(texto_documento, palabra_a_contar)
print("Número de veces que aparece la palabra '{}' en el documento: {}".format(palabra_a_contar, num_apariciones))

# Guardar el texto extraído en un archivo de texto
if texto_documento:
    with open("texto_documento.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_documento)

# Cargar el texto del archivo
archivo_nombre = "texto_documento.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
nltk.download('stopwords')
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabra_funcional in palabras_funcionales:
    print(palabra_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = word_tokenize(texto, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 20 palabras más comunes
distribucion_limpia.plot(20)
