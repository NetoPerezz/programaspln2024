import docx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Función para contar palabras y líneas
def contar_palabras_y_lineas(texto):
    num_palabras = len(texto.split())
    num_lineas = texto.count('\n') + 1
    return num_palabras, num_lineas

# Función para contar la frecuencia de una palabra específica
def contar_apariciones(texto, palabra):
    return texto.lower().count(palabra.lower())

# Función para leer el documento de Word
def leer_documento(nombre_documento):
    try:
        documento = docx.Document(nombre_documento)
        texto_documento = ""
        for parrafo in documento.paragraphs:
            texto_documento += parrafo.text + "\n"
        return texto_documento
    except FileNotFoundError:
        return None

# Pedir al usuario que ingrese el nombre del documento de Word
nombre_documento = input("Ingresa el nombre del documento de Word: ")

# Validar si el documento existe
texto_documento = leer_documento(nombre_documento)
while texto_documento is None:
    print("El documento '{}' no existe. Por favor, ingresa otro nombre de documento.".format(nombre_documento))
    nombre_documento = input("Ingresa el nombre del documento de Word: ")
    texto_documento = leer_documento(nombre_documento)

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

print("----------------------------------------------------------------------")

# Descargar palabras funcionales en español de NLTK
nltk.download('stopwords', quiet=True)
palabras_funcionales = stopwords.words("spanish")
for palabra_funcional in palabras_funcionales:
    print(palabra_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = word_tokenize(texto_documento, language='spanish')
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
