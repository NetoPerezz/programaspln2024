import docx 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Función para contar palabras y líneas
def contar_palabras_lineas(texto):
    num_palabras = len(texto.split())
    num_lineas = texto.count('\n') + 1
    return num_palabras, num_lineas

# Función para contar la frecuencia de una palabra en el texto
def contar_frecuencia_palabra(texto, palabra):
    return texto.lower().count(palabra.lower())

# Cargar el documento .docx
documento = docx.Document("word.docx")

# Extraer el texto del documento
texto_documento = ""
for parrafo in documento.paragraphs:
    texto_documento += parrafo.text + "\n"

# Guardar el texto en un archivo de texto txt
with open("texto_documento.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_documento)

# Contar palabras y líneas
num_palabras, num_lineas = contar_palabras_lineas(texto_documento)
print("Número de palabras en el documento:", num_palabras)
print("Número de líneas de texto en el documento:", num_lineas)

# Contar la frecuencia de una palabra
palabra_buscada = "Python"
frecuencia_palabra = contar_frecuencia_palabra(texto_documento, palabra_buscada)
print("La palabra '{}' aparece {} veces en el documento.".format(palabra_buscada, frecuencia_palabra))

# Cargar el texto del archivo
archivo_nombre = "texto_documento.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
nltk.download('stopwords')
nltk.download('punkt')
palabras_funcionales = set(stopwords.words("spanish"))

# Mostrar algunas palabras funcionales
print("Palabras funcionales en español:")
print(", ".join(palabras_funcionales))

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = word_tokenize(texto, language="spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print("Tokens limpios:")
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 20 palabras más comunes
plt.figure(figsize=(10, 5))
distribucion_limpia.plot(20)
plt.title('Distribución de las 20 palabras más comunes')
plt.xlabel('Palabras')
plt.ylabel('Frecuencia')
plt.show()