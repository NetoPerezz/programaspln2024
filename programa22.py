import nltk
import re

carpeta_nombre="punkt\\"
archivo_nombre="lol.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
lista_frecuencias=distribucion.most_common()
print(lista_frecuencias)

# A esta altura ya tenemos la lista de tokens en "tokens".
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
print(distribucion["Instituto"])