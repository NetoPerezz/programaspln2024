import PyPDF2
import nltk
from nltk import FreqDist
import matplotlib.pyplot as plt

# Abrir el archivo PDF
pdf_file = open('ruta/al/archivo.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extraer el texto del PDF
texto = ''
for page in range(len(pdf_reader.pages)):
    texto += pdf_reader.pages[page].extract_text()

# Cerrar el archivo PDF
pdf_file.close()

# Tokenizar el texto en palabras
tokens = nltk.word_tokenize(texto)

# Contar el número total de palabras
total_palabras = len(tokens)
print(f"Número total de palabras: {total_palabras}")

# Encontrar las palabras que aparecen solo una vez
palabras_unicas = set(palabra for palabra in set(tokens) if tokens.count(palabra) == 1)
print(f"Palabras que aparecen solo una vez: {len(palabras_unicas)}")

# Obtener la distribución de frecuencias de las palabras
freq_dist = FreqDist(tokens)

# Graficar las 20 palabras más comunes
plt.figure(figsize=(12, 6))
freq_dist.plot(20, title="20 palabras más comunes")
plt.show()

# Obtener la distribución de frecuencias de las palabras en formato de texto
print("Distribución de frecuencias:")
for palabra, frecuencia in freq_dist.most_common():
    print(f"{palabra}: {frecuencia}")