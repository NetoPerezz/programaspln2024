import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Descargar recursos necesarios para NLTK (ejecutar una vez)
nltk.download('punkt')

# Función para extraer texto de un PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page in range(num_pages):
            text += reader.getPage(page).extractText()
    return text

# Función para realizar el procesamiento de texto con NLTK
def process_text(text):
    # Tokenización
    tokens = word_tokenize(text)
    
    # Contar palabras totales
    total_words = len(tokens)
    
    # Obtener la distribución de frecuencia
    fdist = FreqDist(tokens)
    
    # Contar palabras que aparecen una sola vez
    unique_words = len(fdist.hapaxes())
    
    # Graficar las 20 palabras más comunes
    fdist.plot(20, title="Top 20 palabras más comunes")
    plt.show()
    
    return total_words, unique_words, fdist

# Ruta del archivo PDF
pdf_path = 'ejemplo.pdf'

# Extraer texto del PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Procesar texto con NLTK
total_words, unique_words, fdist = process_text(pdf_text)

print("Palabras totales:", total_words)
print("Palabras únicas:", unique_words)
